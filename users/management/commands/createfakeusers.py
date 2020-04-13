from faker import Factory

from project.management import BaseCommand
from ...fake import (
    random_cpf,
    create_admin,
    create_default_user,
    random_set,
    create_notifier,
    create_manager,
    create_user,
)
from ...models import User


class Command(BaseCommand):
    help = "Creates fake users"

    def add_arguments(self, parser):
        parser.add_argument("--admin", action="store_true", help="Create an admin@admin.com user")
        parser.add_argument(
            "--admin-password", action="store_true", default="admin", help="Sets the admin password"
        )
        parser.add_argument("--roles", action="store_true", help="Create users with default roles")
        parser.add_argument("--users", type=int, default=0, help="Number of regular users")
        parser.add_argument(
            "--force", action="store_true", help="Force-recreation of special users"
        )
        parser.add_argument("--staging", action="store_true", help="Create the staging database")

    def handle(
        self,
        *files,
        admin=False,
        admin_password=None,
        roles=False,
        users=None,
        force=False,
        staging=False,
        **options,
    ):
        self.inform("Creating fake users", topic=True)
        fake = Factory.create("en-US")
        if staging:
            users = 20

        size = users + int(admin) + int(roles) * 3
        emails = User.objects.values_list("email", flat=True)
        emails = [email.split("@")[0] for email in emails]
        blocked_usernames = {"admin", "user", *emails}
        usernames = random_set(fake.user_name, size, blocked=blocked_usernames)
        cpfs = random_set(random_cpf, size)

        # Create special users with known passwords
        if admin or staging:
            self.mk_user("Admin", create_admin, password=admin_password, force=force)
        if roles or staging:
            user = self.mk_user("Default", create_default_user, force=force)
            self.mk_user("Manager", create_manager, force=force, notifiers=(5, 7), state=user.state)
            self.mk_user("Notifier", create_notifier, force=force, state=user.state)

        # Create regular users
        for _ in range(users // 2):
            create_notifier(
                cpf=cpfs.pop(),
                name=fake.name(),
                password="1234",
                email=usernames.pop() + "@" + fake.domain_name(),
            )

        for _ in range(users - users // 2):
            create_user(
                cpf=cpfs.pop(),
                name=fake.name(),
                password="1234",
                email=usernames.pop() + "@" + fake.domain_name(),
            )

        # Feedback
        n_users = self.style.SUCCESS(str(size))
        self.inform(f"Created {n_users} fake users", depth=1)

    def mk_user(self, kind, fn, **kwargs):
        """
        Try to create user with factory function and return the number of
        created users.
        """
        user, created = fn(**kwargs)
        if created:
            msg = self.style.SUCCESS(kind)
            self.inform(msg + " user created!", depth=1)
        else:
            msg = self.style.WARNING(kind)
            self.inform(msg + " user was already created!", depth=1)
        return user
