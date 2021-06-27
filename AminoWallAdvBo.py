import amino
import pyfiglet
import concurrent.futures
from colorama import init, Fore, Back, Style
init()
print(Fore.CYAN + Style.NORMAL)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("AminoWallAdvBo", font="small"))
print("Wall Advertise Bot For Amino")
client = amino.Client()
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
msg = input("Message/Сообщение: ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
print("""1.Send Wall Advertise to Online Users
2.Send Wall Advertise to Recent Users""")
select = input("Type Number: ")

if select == "1":
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for i in range(1000, 20000, 250):
			for user_id, nickname in zip(sub_client.get_online_users(start=i, size=100).profile.userId, sub_client.get_online_users(start=i, size=100).profile.nickname):
				print(f"Sended Advertise, {nickname} > {user_id}")
				_ = [executor.submit(sub_client.comment, msg, user_id)]
			else:
				break
			print("Sended Wall Advertise to Online Users!")


elif select == "2":
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for i in range(1000, 20000, 250):
			for user_id, nickname in zip(sub_client.get_all_users(type="recent", start=i, size=100).profile.userId, sub_client.get_all_users(type="recent", start=i, size=100).profile.nickname):
				print(f"Sended Advertise, {nickname} > {user_id}")
				_ = [executor.submit(sub_client.comment, msg, user_id)]
			else:
				break
			print("Sended Wall Advertise to Recent Users!")

		
		
