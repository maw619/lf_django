# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Usuarios(models.Model):
    user_key = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_password = models.BinaryField(blank=True, null=True)
    user_nombre = models.CharField(max_length=50, blank=True, null=True)
    user_apellido = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_fk_cia_key = models.IntegerField(blank=True, null=True)
    user_role = models.IntegerField(blank=True, null=True)
    user_address = models.CharField(max_length=100, blank=True, null=True)
    user_llave = models.CharField(max_length=50, blank=True, null=True)
    user_celular = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios'
    
        def __str__(self):
            return self.user_name


class AppLfcargos(models.Model):
    ch_key = models.IntegerField(primary_key=True)
    ch_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfcargos'


class AppLfcertificados(models.Model):
    cer_key = models.IntegerField(primary_key=True)
    cer_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfcertificados'


class AppLfempcer(models.Model):
    ec_key = models.IntegerField(primary_key=True)
    ec_fk_emp_key = models.IntegerField(blank=True, null=True)
    ec_fk_cer_key = models.IntegerField(blank=True, null=True)
    ec_exp_yyyymmdd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfempcer'


class AppLfemployees(models.Model):
    emp_key = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=70, blank=True, null=True)
    emp_fk_ch_key = models.IntegerField(blank=True, null=True)
    emp_email = models.CharField(max_length=80, blank=True, null=True)
    emp_phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfemployees'


class AppLfphotos(models.Model):
    ph_key = models.IntegerField(primary_key=True)
    ph_fk_rep_key = models.IntegerField(blank=True, null=True)
    ph_link = models.CharField(max_length=65535, blank=True, null=True)
    ph_yyyymmdd = models.CharField(max_length=50, blank=True, null=True)
    ph_desc = models.CharField(max_length=65535, blank=True, null=True)
    ph_user_name = models.CharField(max_length=50, blank=True, null=True)
    ph_obs = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfphotos'


class AppLfphotos2(models.Model):
    id = models.BigAutoField(primary_key=True)
    ph_key2 = models.IntegerField(blank=True, null=True)
    ph_fk_rep_key2 = models.IntegerField(blank=True, null=True)
    ph_fk_ph_key = models.IntegerField(blank=True, null=True)
    ph_link2 = models.CharField(max_length=65535, blank=True, null=True)
    ph_yyyymmdd2 = models.CharField(max_length=50, blank=True, null=True)
    ph_desc2 = models.CharField(max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfphotos2'


class AppLfprojects(models.Model):
    pr_key = models.IntegerField(primary_key=True)
    pr_desc = models.CharField(max_length=150, blank=True, null=True)
    pr_address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfprojects'


class AppLfrepemails(models.Model):
    repe_key = models.IntegerField(primary_key=True)
    repe_fk_rep_key = models.IntegerField(blank=True, null=True)
    repe_fk_emp_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfrepemails'


class AppLfreportes(models.Model):
    rep_key = models.IntegerField(primary_key=True)
    rep_name = models.CharField(max_length=80, blank=True, null=True)
    rep_fk_emp_key = models.IntegerField(blank=True, null=True)
    rep_fk_emp_key_sup = models.IntegerField(blank=True, null=True)
    rep_fk_pr_key = models.IntegerField(blank=True, null=True)
    rep_desc = models.CharField(max_length=255, blank=True, null=True)
    rep_user_name = models.CharField(max_length=50, blank=True, null=True)
    rep_send = models.IntegerField(blank=True, null=True)
    rep_send_email = models.CharField(max_length=80, blank=True, null=True)
    rep_notes = models.CharField(max_length=255, blank=True, null=True)
    rep_yyyymmdd = models.CharField(max_length=50, blank=True, null=True)
    rep_ws_to = models.CharField(max_length=255, blank=True, null=True)
    rep_pages = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_lfreportes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
