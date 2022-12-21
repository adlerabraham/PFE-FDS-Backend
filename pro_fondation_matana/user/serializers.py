from rest_framework.serializers import ModelSerializer, Serializer, ValidationError, CharField, EmailField
from rest_framework.validators import UniqueValidator
from user.models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.exceptions import AuthenticationFailed
from userprofile.models import Student, Teacher



class User_serializer(ModelSerializer):

    class Meta:
        model = User      
        fields = '__all__'



MIN_LENGTH =3

class Register_user_serializer(ModelSerializer):
   
    password = CharField(
        write_only=True, 
        min_length=MIN_LENGTH, 
        error_messages ={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
         }
    ) 

    initial_password = CharField(
        write_only=True, 
        min_length=MIN_LENGTH, 
        error_messages ={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    class Meta:
        model = User

        fields = (
                "username",
                "first_name",
                "last_name",
                "sex",
                "email",
                "birth_date",
                "blood_type",
                "address",
                "password",
                "initial_password",
                "phone_number",
                "is_superuser",
                "is_staff",
                "groups",
                "user_permissions",
            )    

      
        extra_kwargs= {
            "password": {"write_only": True},
            "email": {
                "required" : True,
                "allow_blank": False,
                "validators":[
                        UniqueValidator(
                        User.objects.all(),"A user with that Email already exists"
                    )
                ]
                

            }
                }


    def validate(self, data):

        groups = self.initial_data["groups"] 

        if data["password"] != data["initial_password"]:
            raise ValidationError("Passwords don't match")
        data["groups"] = groups
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            blood_type =  validated_data["blood_type"],
            birth_date =  validated_data["birth_date"], 
            address =  validated_data["address"],  
            sex =  validated_data["sex"],  
            is_superuser =  validated_data["is_superuser"], 
            is_staff = validated_data ["is_staff"],
            initial_password = validated_data ["initial_password"],

            )

        user.user_permissions.set(validated_data["user_permissions"])
        user.groups.set(validated_data["groups"])
        user.set_password(validated_data["password"])

        if self.context['request'].user.is_authenticated:
            user.created_by = self.context['request'].user.username
        else:
            user.created_by = validated_data["username"]

        user.save()

        group_id = validated_data["groups"][0] 
        print(group_id) 
        group = Group.objects.get(id=group_id)
       
        if group.id == 4:
                Student.objects.create(User=user, responsible_person='', relationship='', phone_number='', created_by=user.created_by,)
            
        elif group.id == 3:
                Teacher.objects.create(User=user)
       
        return user


    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance




class Update_user_serializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
                #"username",
                "first_name",
                "last_name",
                "sex",
                "birth_date",
                "blood_type",
                "address",             
                "phone_number",
                
            )           
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise ValidationError({"username": "This username is already in use."})
        return value


    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance

def delete_user_instance(request, user: User) -> None:
    user.is_deleted_by = request.user.username
    user.soft_delete()





    # def update(self, instance, validated_data):
    #     user = self.context['request'].user

    #     if user.pk != instance.pk:
    #         raise ValidationError({"authorize": "You dont have permission for this user."})

    #     instance.username = validated_data["username"],
    #     instance.first_name = validated_data["first_name"],
    #     instance.last_name = validated_data["last_name"],
    #     instance.groupe_sanguin =  validated_data["groupe_sanguin"],
    #     instance.date_naissance =  validated_data["date_naissance"], 
    #     instance.adresse =  validated_data["adresse"],  
    #     instance.sexe =  validated_data["sexe"],  
    #     instance.photo_profil = validated_data ['photo_profil']  
          

    #     instance.save()

    #     return instance




class Update_email_serializer :

    password = CharField(
        write_only=True, 
        required=True
    )    
    
    class Meta:
        model = User
        fields = ( 'password','email')
        # extra_kwargs = {
        #     'password': {'required': True},
        # }
    
    def validate_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError({"password": "password is not correct"})
        return value

    def save(self, **kwargs):
        self.instance.is_verified = False
        self.instance.email = self.validated_data['email']
        return super().save(**kwargs)


    def update(self, instance, validated_data):
        if instance.is_verified:
            instance.email = validated_data['email']
        instance = super().update(instance, validated_data)
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance








class Change_password_serializer(ModelSerializer):
    password = CharField(
        write_only=True, 
        min_length=MIN_LENGTH, 
        error_messages ={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
         }
    ) 

    password2 = CharField(
        write_only=True, 
        min_length=MIN_LENGTH, 
        error_messages ={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
            #validators=[validate_password])
         }
    ) 
    
    
    old_password = CharField(
        write_only=True, 
        required=True
    )


    class Meta:
        model = User
        fields = ('old_password', 
                  'password', 
                  'password2',
                  )


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError({"old_password": "Old password is not correct"})
        return value

    # def update(self, instance, validated_data):
    #     instance.initial_password = " " 
    #     instance.set_password(validated_data['password'])
    #     instance.save()

    #     return instance

    def update(self, instance, validated_data):
        instance.initial_password = " " 
        instance.set_password(validated_data["password"])
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance




class Reset_password_send_email_serializer(Serializer):

    username = CharField(max_length = 100)
    email=EmailField(min_length = 2)

    class Meta:
        fields = ['email' , 'username']



class Set_new_password_serializer(Serializer):

    #password = CharField(write_only=True, required=True, validators=[validate_password])
    password = CharField(
        min_length = 3, 
        max_length = 68, 
        write_only = True
        )

    password2 = CharField(
        min_length = 3, 
        max_length = 68, 
        write_only = True
        )

    token = CharField(min_length = 1, 
    max_length = 68,
    write_only = True
    )

    uidb64 = CharField(
        min_length = 1, 
        max_length = 68, 
        write_only = True
        )
    class Meta:
        fields = ['password', 'password2', 'token', 'uidb64']

        
    def validate(self,attrs):
        try: 
            
            password = attrs.get('password')
            password2 = attrs.get('password2')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if password != password2:
                raise ValidationError({"password": "Password fields didn't match."})


            elif not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed ('The reset link is invalid', 401)

            if self._context['request'].user.is_authenticated:
                updated_by = self._context['request'].user.username
            else:
                updated_by = user.username                
  
  
            user.set_password(password)
            user.updated_at = timezone.now()
            user.updated_by = updated_by
            user.save()
            return (user)


        except ValidationError as identifier :
            raise ValidationError({"password": "Password fields didn't match."})

        except AuthenticationFailed as identifier :
            raise AuthenticationFailed ('The reset link is invalid', 401)
        
        except Exception as e :
            raise AuthenticationFailed ("Token Invalid", 401)
   
        
        return super().validate(attrs)
