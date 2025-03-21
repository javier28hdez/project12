from rest_framework import serializers
from user_app.models import Account
from rest_framework.exceptions import ValidationError


class AccountSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type':'password'},max_length=128, write_only=True)

    class Meta:
        model = Account
        fields = ['username','password','email', 'password_confirmation', 'direccion', 'telephone']
        extra_kwargs = {
            'password':{'write_only':True}
        }


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password2 = attrs.get('password_confirmation')
        username = attrs.get('username')
        direccion  = attrs.get('direccion')
        telephone = attrs.get('telephone')
        #request = self.context.get('request')

        if password != password2:
            raise ValidationError("Verifique los campos que sean correctos")
        
        if Account.objects.filter(email=email).exists():
            raise ValidationError("La cuenta ya existe")

        return{
          'email':email,
          'username':username,
          'password':password,
          'direccion':direccion,
          'telephone':telephone 
        } 


    def save(self):
        account = Account.objects.create_user(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            direccion=self.validated_data.get('direccion'),
            telephone=self.validated_data.get('telephone'),
            password=self.validated_data.get('password')
        )
        return account
