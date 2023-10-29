from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name



class Country(models.Model):
    country_name= models.CharField(max_length=50, blank = True)
    country_id =models.IntegerField()

    def __str__(self) -> str:
        return self.country_name

class State(models.Model):
    state_name= models.CharField(max_length=50)
    state_id =models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)   
    def __str__(self) -> str:
        return self.state_name    

class City(models.Model):
    city_name= models.CharField(max_length=50)
    city_id =models.IntegerField()
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.city_name