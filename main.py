from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
import subprocess
import requests
import myport
from kivy.core.window import Window
Window.softinput_mode = "below_target"

KV = '''
#:import Clock kivy.clock.Clock
ScreenManager:
    MenuScreen:


<MenuScreen>:
    name:"menu"
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Ping'
            icon: 'access-point-network'

            BoxLayout:
            	orientation:"vertical"
            	MDToolbar:
            		title: "Ping"
            		specific_text_color: 1,1,1,1
	            TextInput:
	            	id:displaybox
	            	text: "$ "
	            	size_hint_y:None
	            	height:100
	            	disabled_foreground_color: 1,1,1,1
	            	border: 10,10,10,10
	            	background_color:1,1,1,0
	            	foreground_color:1,1,1,1
					readonly:True

            	FloatLayout:
	            	MDTextField:
	            		id: textbox
    					hint_text: "Enter Url here"
    					helper_text: "eg.. http://www.URL.com"
    					helper_text_mode: "persistent"
    					multiline: False
    					mode:"fill"
    					line_color_normal: 0,0,0,1
    					icon_left: 'earth'
					FloatLayout:
						MDFloatingActionButton:
							icon: "play"
							elevation_normal: 8
							pos_hint: {"x":0.02, "y":.1}
							on_release:
								displaybox.text = ""
								displaybox.text="$ "+app.menu.ping(root.ids.textbox.text)
						MDFloatingActionButton:
							icon: "delete-forever"
							elevation_normal: 8
							pos_hint: {"right":.98, "y":.1}
							on_release:
								displaybox.text = "$"
								textbox.text= ""

        MDBottomNavigationItem
            name: 'screen 2'
            text: 'Host Checker'
            icon: 'check-network'

            BoxLayout:
            	orientation:"vertical"
            	MDToolbar:
            		title: "Host Checker"
            		specific_text_color: 1,1,1,1
	            ScrollView:
					id: scrlv
		            TextInput:
		            	id:displaybox2
		            	text: "$ "
		            	size_hint_y:None
		            	disabled_foreground_color: 1,1,1,1
		            	border: 10,10,10,10
		            	background_color:1,1,1,0
		            	allow_copy:True
		            	multiline:True
		            	use_bubble:True
		            	foreground_color:1,1,1,1
						cursor:0,0
						readonly:True
						on_touch_down: Clock.schedule_once(lambda dt: self.select_all())
						height: max(self.minimum_height, scrlv.height)

	            FloatLayout:
	            	MDTextField:
	            		id:textbox2
						text: textbox.text
    					hint_text: "Enter Url here"
    					helper_text: "eg.. http://www.URL.com"
    					helper_text_mode: "persistent"
    					multiline: False
    					mode:"fill"
    					line_color_normal: 0,0,0,1

    				BoxLayout:
    					orientation:"horizontal"
    					pos_hint: {"x":0,"y":.4}
					    MDRectangleFlatIconButton:
					        text: 'GET'
					        icon: 'check-network'
					        on_release:
					        	displaybox2.text= "Get response:\\n"+ app.menu.get(textbox2.text)
								displaybox2.cursor = 0,0
								
					    MDRectangleFlatIconButton:
					        text: 'POST'
					        icon: 'cloud-upload'
					        on_release:
					        	displaybox2.text= "Post response:\\n"+app.menu.post(textbox2.text)
								displaybox2.cursor = 0,0
					        
					    MDRectangleFlatIconButton:
					        text: 'PUT'
					        icon: 'file-upload'
					        on_release:
					        	displaybox2.text="Put response:\\n"+app.menu.get(textbox2.text)
								displaybox2.cursor = 0,0
					    
					BoxLayout:
						orientation:"horizontal" 
						pos_hint: {"x":0,"y":.25}   
					    MDRectangleFlatIconButton:
					        text: 'HEAD'
					        icon: 'format-header-pound'
					        on_release:
					        	displaybox2.text="Head response:\\n"+app.menu.get(textbox2.text)
								displaybox2.cursor = 0,0
					        
					    MDRectangleFlatIconButton:
					        text: 'DELETE'
					        icon: 'delete'
					        on_release:
					        	displaybox2.text="Delete response:\\n"+app.menu.get(textbox2.text)
								displaybox2.cursor = 0,0

					    MDRectangleFlatIconButton:
					        text: 'OPTIONS'
					        icon: 'cloud-question'
					        on_release:
					        	displaybox2.text="Options response:\\n"+app.menu.get(textbox2.text)
								displaybox2.cursor = 0,0
					FloatLayout:
						MDFloatingActionButton:
							text: 'CLEAR'
							icon: 'delete-forever'
							color: 1,.1,.1,1
							pos_hint: {"right":.98,"y":.1}
							on_release:
								textbox2.text=""
								displaybox2.text="$"

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Port Scanner'
            icon: 'information'

            BoxLayout:
            	orientation:"vertical"
            	MDToolbar:
            		title: "Port Scanner"
            		specific_text_color: 1,1,1,1

	            TextInput:
					id:displaybox3
	            	text: """Coming Soon..."""
	            	size_hint_y:None
	            	height:100
	            	disabled_foreground_color: 1,1,1,1
	            	border: 10,10,10,10
	            	background_color:1,1,1,0
	            	foreground_color:1,1,1,1
					readonly:True

	            FloatLayout:
					MDTextField:
	            		id:textbox3
						text: textbox.text
    					hint_text: "Enter Url here"
    					helper_text: "eg.. http://www.URL.com"
    					helper_text_mode: "persistent"
    					multiline: False
    					mode:"fill"
    					line_color_normal: 0,0,0,1
					FloatLayout:
						MDFloatingActionButton:
							icon: "delete-forever"
							elevation_normal: 8
							pos_hint: {"x":.02, "y":.1}
							on_release:
								displaybox3.text = "$"
								textbox3.text= ""

						MDFloatingActionButton:
							icon: "play"
							color:0,1,0,.5
							elevation_normal: 8
							pos_hint: {"right":.98, "y":.1}
							on_release:
								displaybox3.text = ""
								displaybox3.text="$ Ports:"+app.menu.scan(root.ids.textbox.text)
					
'''
class MenuScreen(Screen):

	def scan(self,url):
		sc = myport.Scanner(url,1,1024,3)
		sc.scan()
		return str(sc.open_ports)

	def ping(self,host):
		host = host.replace('https//:','')
		host = host.replace('http//:','')
		command = ['ping','-c','1',host]
		resp = subprocess.call(command)
		if resp ==0:
			return "Packets recieved host is up..."
		else:	
			return "No Packets recieved host is down or incorrect url."

	def get(self,host):
		resp = 0
		try:
			r = requests.get("https://"+host)
			str_r = r.headers
			s_out =""
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
			return s_out
		return "status code:"+str(resp)+"\n"+s_out

	def post(self,host):
		try:
			r = requests.post("https://"+host)
			str_r = r.headers
			s_out =""
			resp = 0
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
			return s_out
		return "status code:"+str(resp)+"\n"+s_out
	def put(self,host):
		try:
			r = requests.put("https://"+host)
			str_r = r.headers
			s_out =""
			resp = 0
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
			return s_out
		return "status code:"+str(resp)+"\n"+s_out

	def head(self,host):
		try:
			r = requests.head("https://"+host)
			str_r = r.headers
			s_out =""
			resp = 0
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
			return s_out
		return "status code:"+str(resp)+"\n"+s_out

	def delete(self,host):
		try:
			r = requests.delete("https://"+host)
			str_r = r.headers
			s_out =""
			resp = 0
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
			return s_out
		return "status code:"+str(resp)+"\n"+s_out
	def options(self,host):
		try:
			r = requests.options("https://"+host)
			str_r = r.headers
			s_out =""
			resp = 0
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
			return s_out
		return "status code:"+str(resp)+"\n"+s_out

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'
        return  Builder.load_string(KV)

    menu = MenuScreen()
    
if __name__ == "__main__":
	MainApp().run()