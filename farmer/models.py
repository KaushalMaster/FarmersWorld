from django.db import models

# Create your models here.


class farmer_details(models.Model):
    f_id = models.AutoField()
    f_fname = models.CharField(max_length=25)
    f_lname = models.CharField(max_length=25)
    f_img = models.ImageField()
    f_address = models.CharField(max_length=100)
    f_area = models.CharField(max_length=50)
    f_city = models.CharField(max_length=25)
    f_state = models.CharField(max_length=25)
    f_password = models.CharField(max_length=25)
    f_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.f_fname + ' ' + self.f_lname


class customer_details(models.Model):
    c_id = models.AutoField()
    c_fname = models.CharField(max_length=25)
    c_lname = models.CharField(max_length=25)
    c_img = models.ImageField()
    c_address = models.CharField(max_length=100)
    c_area = models.CharField(max_length=50)
    c_city = models.CharField(max_length=25)
    c_state = models.CharField(max_length=25)
    c_password = models.CharField(max_length=25)
    c_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.c_fname + ' ' + self.c_lname


class product_details(models.Model):
    p_id = models.AutoField()
    p_name = models.CharField(max_length=25)
    p_price = models.FloatField()
    p_type = models.CharField(max_length=25)
    p_img = models.ImageField()
    p_desc = models.CharField(max_length=100)
    p_isAvailable = models.BooleanField()

    def __str__(self) -> str:
        return self.p_name


class farmer_order(models.Model):
    o_fid = models.CharField()
    o_id = models.AutoField()
    o_pid = models.CharField()
    o_qty = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.o_fid


class payment_details(models.Model):
    pmt_id = models.AutoField()
    pmt_oid = models.CharField()
    pmt_amt = models.FloatField()
    pmt_cid = models.CharField()

    def __str__(self) -> str:
        return self.pmt_id
