from user_app.controllers.serializers.AccountSerializer import AccountSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate
from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, OpenApiParameter

@extend_schema(
    summary="Registra usuarios",
    description="Endpoint para registrar usuarios",
    request=AccountSerializer(),
    responses={201: AccountSerializer()}
)
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        data={}
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()

            token=Token.objects.get(user=account)
            data['email']=account.email
            data['token']=token.key
            data['response']='Se ha registrado correctamente'
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@extend_schema(
    summary="Autenticar usuarios",
    description="Endpoint para autenticar el usuarios",
    examples=[
        OpenApiExample(
            "Ejemplo de solicitud",
            value={"email": "ana@gmail.com", "password": "123"},
        ),
    ],
    parameters=[
        OpenApiParameter(
            name="email",
            type=str,
            description="email del usuario",
            required=True
        ),
        OpenApiParameter(
            name="password",
            type=str,
            description="password del usuario",
            required=True
        ),
    ],
    responses={
        202: OpenApiResponse(description='se registro con exito'),
        400: OpenApiResponse(description='error con los datos enviados'),
        403: OpenApiResponse(description='el usuario se encuentra autenticado')
    }
)        
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        email=request.data.get('email')
        password=request.data.get('password')

        user = authenticate(request=request, email=email, password=password)

        if user is not None:
            login(request, user)

            try:
                token=Token.objects.create(user=user)
                data={
                    'token':token.key,
                } 
                return Response(data, status=status.HTTP_202_ACCEPTED)
            
            except Exception as e:
                return Response({'response':'El usuario se encuentra authenticado'}, status=status.HTTP_403_FORBIDDEN)
        
        Response({'errors':'Ha ocurrido un error'},status=status.HTTP_400_BAD_REQUEST)


#logout
@extend_schema(
    summary="Logout usuarios",
    description="Endpoint para logout a los usuarios",
    examples=[
        OpenApiExample(
            "Ejemplo de solicitud",
            value={"token": "laksnofnpwfe"},
        )
    ],
    parameters=[
        OpenApiParameter(
            name="token",
            type=str,
            description="token del usuario",
            required=True
        )
    ],
    responses={
        200: OpenApiResponse(description='se logout con exito'),
    }
) 
#Por un JSON recivo un token
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



    
        