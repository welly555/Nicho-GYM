from models import Academia

login = Academia.objects.filter(E_mail="Kamile@gmail.com").exists()

print(login)
