from django.db import models
from django.utils.safestring import mark_safe
# from PIL import Image
# import psycopg2
# from gcloud import storage

# Create your models here.

class Product(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    cost = models.IntegerField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=100, editable=False)
    review = models.CharField(blank=True, null=True, max_length=100)
    classify = models.CharField(blank=True, null=True, max_length=100)
    # image = models.CharField(blank=True, null=True, max_length=100, editable=False)

    def __str__(self):
        return self.name
    # def image_front(self):
    #     return mark_safe('<a href="%s" target="_blank"><img src="%s" width="150" height="150" /></a>' % (self.image, self.image))
    # image_front.short_description = 'Product image'
    # image_front.allow_tags = True
    
    def description_s(self):
        start = '<html><body><textarea rows="10" cols="50" maxlength="50" id="field3" name="description_s">'
        end = '</textarea><div class="text-right mt-1" id="3"></div><script>document.addEventListener(\'DOMContentLoaded\', function() {const messageEle = document.getElementById(\'field3\');const counterEle = document.getElementById(\'3\');messageEle.addEventListener(\'input\', function(e) {const target = e.target;const maxLength = target.getAttribute(\'maxlength\');const currentLength = target.value.length;counterEle.innerHTML = `${currentLength}/${maxLength}`;});});</script></body></html>'
        final = start + str(self.description) + end
        return mark_safe(final)
    description_s.short_description = 'information'
    description_s.allow_tags = True
    
    # def classification(self):
    #     temp_s = '<p>'
    #     temp_e = '</p>'
    #     try:
    #         temp_m = self.classify
    #     except:
    #         temp_m = ""
    #     final = temp_s + temp_m + temp_e
    #     return mark_safe(final)
    # classification.short_description = 'classification'
    # classification.allow_tags = True
    
    class Meta:
        managed = False
        db_table = 'product'



class Classification(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    classification = models.CharField(blank=True, null=True, max_length=100)
    def __str__(self):
        tmp = self.product.name
        return tmp
    class Meta:
        managed = False
        db_table = 'classify'