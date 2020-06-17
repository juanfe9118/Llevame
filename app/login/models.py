from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Department(models.Model):
    """
        Department Model
        Attributtes:
        - Name
        - Code
    """
    name = models.CharField(max_length=32, blank=False, null=False)
    code = models.IntegerField(null=False)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})


class City(models.Model):
    """
        City Model

    """
    department = models.ForeignKey(Department,
                                   verbose_name=("department"),
                                   on_delete=models.CASCADE,
                                   null=True)
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=32, default="")

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("City_detail", kwargs={"pk": self.pk})


class UserManager(BaseUserManager):
    """ User manager model """
    def create_user(self, first_name=None, last_name=None,
                    type_id=None, n_document=None,
                    department=None, city=None,
                    picture=None, email=None,
                    password=None):
        """ Create a user """
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not type_id:
            raise ValueError("User must have a type id")
        if not n_document:
            raise ValueError("User must have a document")
        if not department:
            raise ValueError("User must have a department")
        if not city:
            raise ValueError("User must have a city")
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
               first_name=first_name,
               last_name=last_name,
               type_id=type_id,
               n_document=n_document,
               department=department,
               city=city,
               picture=picture,
               email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name,
                         type_id, n_document,
                         department, city,
                         email, password):
        """ Method that creates a superuser """
        user = self.create_user(
               first_name=first_name,
               last_name=last_name,
               type_id=type_id,
               n_document=n_document,
               department=Department.objects.get(id=department),
               city=City.objects.get(id=city),
               email=self.normalize_email(email),
               password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def validate_image(self, picture):
        """ Validate some picture values """
        if picture:
            if picture.size > 2000000:
                raise ValueError('Max size allowed 2MB')
            if picture.image.width < 180:
                raise ValueError('Width should be min 180px')
            if picture.image.height < 180:
                raise ValueError('Height should be min 180px')


class User(AbstractBaseUser):
    """
        User Model
        Attributes:
        - First name
        - Last name
        - Email
        - Type of ID
        - ID (n_document)
        - Picture
        - Department
        - City
        - Is_driver
    """
    first_name = models.CharField(max_length=32, blank=False, null=False)
    last_name = models.CharField(max_length=32, blank=False, null=False)
    type_id = models.CharField(max_length=2, blank=False, null=False)
    n_document = models.CharField(max_length=32, blank=False,
                                  null=False, unique=True)
    department = models.ForeignKey(Department,
                                   verbose_name=("department"),
                                   on_delete=models.CASCADE,
                                   blank=False, null=False)
    city = models.ForeignKey(City,
                             verbose_name=("city"),
                             on_delete=models.CASCADE,
                             blank=False, null=False)
    # pillow necessary to user imagefield
    picture = models.ImageField(upload_to='pictures', height_field=None,
                                width_field=None, max_length=None,
                                blank=True, null=True)
    email = models.EmailField(max_length=90, blank=False,
                              null=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'type_id', 'n_document',
                       'department', 'city']

    # Manager Class
    objects = UserManager()

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")
        ordering = ['id']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


# Create a token when a user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
