_S='desktop'
_R='Discord'
_Q='windows'
_P=''
_O=''
_N='properties'
_M='heartbeat_interval'
_L='Channel ID: '
_K='Server ID: '
_J='tokens.txt'
_I="Don't forget to put your tokens in Tokens.txt"
_H='self_deaf'
_G='self_mute'
_F='channel_id'
_E='guild_id'
_D=False
_C=True
_B='op'
_A='d'
from pystyle import*
import os
from colorama import*
import time,asyncio,json,websockets
from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import random
os.system('clear'if os.name=='posix'else'cls')
intro='\n██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██╗   ██╗ ██████╗ ██╗ ██████╗███████╗\n██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██║   ██║██╔═══██╗██║██╔════╝██╔════╝\n██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║   ██║██║   ██║██║██║     █████╗         by ayhu\n██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝         \n██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗\n╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝\n                                                                                             \n                                    > Press Enter                                         \n\n'
Anime.Fade(Center.Center(intro),Colors.red_to_yellow,Colorate.Vertical,interval=.035,enter=_C)
print(f"""{Fore.LIGHTBLUE_EX}
      

██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██╗   ██╗ ██████╗ ██╗ ██████╗███████╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██║   ██║██╔═══██╗██║██╔════╝██╔════╝
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║   ██║██║   ██║██║██║     █████╗         
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝         
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝
                                                                                             
           

""")
time.sleep(1)
Write.Print('\nWhich option do you want to choose: ',Colors.red_to_yellow)
Write.Print('\n> 1 - join voice ',Colors.red_to_yellow)
Write.Print('\n> 2 - voice spam ',Colors.red_to_yellow)
Write.Print('\n> 3 - exit ',Colors.red_to_yellow)
askim=int(input('\nchoice: '))
if askim==1:
	print(_I)
	with open(_J,'r')as token_file:tokens=token_file.readlines();server_id=input(_K);channel_id=input(_L)
	async def connect(token):
		async with websockets.connect('wss://gateway.discord.gg/?v=9&encoding=json')as websocket:
			hello=await websocket.recv();hello_json=json.loads(hello);heartbeat_interval=hello_json[_A][_M];await websocket.send(json.dumps({_B:2,_A:{'token':token.strip(),_N:{'':_Q,_O:_R,_P:_S}}}));await websocket.send(json.dumps({_B:4,_A:{_E:server_id,_F:channel_id,_G:_D,_H:_D}}))
			while _C:
				await asyncio.sleep(heartbeat_interval/1000)
				try:await websocket.send(json.dumps({_B:1,_A:None}))
				except Exception:break
	async def main():
		tasks=[]
		for token in tokens:task=asyncio.create_task(connect(token));tasks.append(task)
		await asyncio.gather(*tasks)
	asyncio.run(main())
elif askim==2:
	print(_I);tokenlist=open(_J,'r').read().splitlines();server=int(input(_K));channel=int(input(_L));deaf=input('Defean: (y/n) ')
	if deaf=='y':deaf=_C
	if deaf=='n':deaf=_D
	mute=input('Mute: (y/n) ')
	if mute=='y':mute=_C
	if mute=='n':mute=_D
	stream=input('Stream: (y/n) ')
	if stream=='y':stream=_C
	if stream=='n':stream=_D
	video=input('Video: (y/n) ')
	if video=='y':video=_C
	if video=='n':video=_D
	executor=ThreadPoolExecutor(max_workers=int(1000))
	def run(token):
		B='self_video';A='self_stream?';ws=WebSocket();ws.connect('wss://gateway.discord.gg/?v=8&encoding=json');hello=loads(ws.recv());heartbeat_interval=hello[_A][_M];ws.send(dumps({_B:2,_A:{'token':token,_N:{'':_Q,_O:_R,_P:_S}}}));ws.send(dumps({_B:4,_A:{_E:server,_F:channel,_G:mute,_H:deaf,A:stream,B:video}}));ws.send(dumps({_B:18,_A:{'type':'guild',_E:server,_F:channel,'preferred_region':'singapore'}}));stay_duration=1;wait_duration=1
		while _C:sleep(stay_duration);ws.send(dumps({_B:4,_A:{_E:server,_F:None,_G:mute,_H:deaf,A:stream,B:video}}));sleep(wait_duration);ws.send(dumps({_B:4,_A:{_E:server,_F:channel,_G:mute,_H:deaf,A:stream,B:video}}))
	os.system(f"title Total Tokens: {len(tokenlist)}");i=0
	for token in tokenlist:executor.submit(run,token);i+=1;print('[+] Joined voice channel');sleep(random.uniform(.1,.1))
elif askim==3:print('Exiting the program...')
else:print('You have entered invalid. Please try again.')
