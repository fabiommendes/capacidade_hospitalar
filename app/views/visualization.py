import datetime
import io

import humanize
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from . import models
from ..utils import parse_date

CAPACITY_FIELDS = ["beds_adults", "beds_pediatric", "icu_adults", "icu_pediatric"]
plt.style.use("ggplot")


@login_required
def plot_healthcare_unit_capacity(request, cnes_id, start_date=None):
    unit = get_object_or_404(models.HealthcareUnit, cnes_id=cnes_id)
    user = request.user
    if settings.DEBUG and user.is_superuser:
        pass
    elif not user.is_notifier or not user.healthcare_units.filter(pk=unit.pk).exists():
        raise Http404

    # Query db
    qs = unit.capacity_notifications.all()
    if start_date:
        date = parse_date(start_date)
        qs = qs.filter(date__gte=date)
    cols = ["date", *CAPACITY_FIELDS]

    # Prepare raw data
    data = list(qs.values_list(*cols))
    if not data:
        data = [[now().date(), *([0] * (len(cols) - 1))]]
    data = np.array(data)

    # Prepare dataframe
    df = pd.DataFrame(data, columns=cols)
    if len(df) == 1:
        day = datetime.timedelta(days=1)
        first = pd.DataFrame(df.values, columns=cols)
        first.iloc[0, 0] -= day
        df = first.append(df)
    df.index = df.pop("date")
    df = df.sort_index()
    df = pd.DataFrame(
        {
            "Clínicos": df[["beds_adults", "beds_pediatric"]].sum(1),
            "UTI": df[["icu_adults", "icu_pediatric"]].sum(1),
        }
    )

    # Prepare plot
    fig, ax = plt.subplots()
    df.plot.bar(ax=ax, rot=45)
    df.index.label = "Datas"
    ax.margins()
    ax.set_xlabel(None)
    ax.set_ylabel("Capacidade (número leitos)")
    ax.set_xticklabels([d.strftime("%x") for d in df.index])
    data = plt_svg(fig)
    return HttpResponse(data, content_type="image/svg+xml")


def plt_svg(fig=None) -> str:
    """Return a string with """

    if fig is None:
        fig = plt.gca()
    fd = io.StringIO()
    fig.savefig(fd, format="svg", bbox_inches="tight")
    return fd.getvalue()


def adj_dates(angle=0, pretty=False, ax=None):
    """
    Adjust dates in the horizontal label of a matplotlib plot.
    """
    if ax is None:
        ax = plt.gca()
    xs = ax.get_xticks()
    labels = None
    if pretty:
        pretty = (lambda x: humanize.naturaldate(x).title()) if pretty is True else pretty
        labels = [pretty(datetime.date.fromordinal(int(x))) for x in xs]
    ax.set_xticks(xs, labels)
    ax.tick_params("x", labelrotation=angle)


pre, pos = settings.LANGUAGE_CODE.split("-")
humanize.i18n.activate(f"{pre}_{pos.upper()}")
