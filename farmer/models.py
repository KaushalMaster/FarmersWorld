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
    # o_fid = # TODO:@KaushalMaster CHECK IF o_fid IN farmer_details
    o_id = models.AutoField()

    def __str__(self) -> str:
        return 'f_name'  # TODO:@KaushalMaster GET f_name USING o_fid


class order_product(models.Model):
    # o_id = # TODO:@KaushalMaster FOR EACH ORDER IN farmer_order
    # o_pid = models. # TODO:@KaushalMaster FOREIGN KEY
    o_qty = models.PositiveIntegerField()

    def __str__(self) -> str:
        return 'p_name'  # TODO:@KaushalMaster GET p_name USING o_pid


class payment_details(models.Model):
    pmt_id = models.AutoField()
    # pmt_oid = # TODO:@KaushalMaster CHECK IF pmt_oid IN farmer_order
    pmt_amt = models.FloatField()
    # pmt_cid = # TODO:@KaushalMaster CHECK IF pmt_cid IN customer_details

    def __str__(self) -> str:
        # TODO:@KaushalMaster GET c_name USING pmt_cid
        return str(self.pmt_id) + 'c_name'
