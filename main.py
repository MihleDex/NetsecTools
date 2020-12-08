from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
import subprocess
import requests
from kivy.core.window import Window
import pprint

Window.softinput_mode = "below_target"

KV = '''
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
    				MDFloatingActionButton:
    					icon: "play"
    					elevation_normal: 8
    					pos_hint: {"right":.98, "y":.1}
    					on_release:
    						displaybox.text = ""
    						displaybox.text="$ "+app.menu.ping(root.ids.textbox.text)
    				MDFloatingActionButton:
    					icon: "delete-forever"
    					elevation_normal: 8
    					pos_hint: {"x":0.01, "y":.1}
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
		            TextInput:
		            	id:displaybox2
		            	text: "$ "
		            	size_hint_y:1
		            	disabled_foreground_color: 1,1,1,1
		            	border: 10,10,10,10
		            	background_color:1,1,1,0
		            	allow_copy:True
		            	multiline:True
		            	use_bubble:True
		            	foreground_color:1,1,1,1

	            FloatLayout:
	            	MDTextField:
	            		id:textbox2
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
					        	displaybox2.text= "get response:\\n"+ app.menu.get(textbox2.text)


					    MDRectangleFlatIconButton:
					        text: 'POST'
					        icon: 'cloud-upload'
					        on_release:
					        	displaybox2.text= "post response: "+app.menu.get(textbox2.text)
					        
					    MDRectangleFlatIconButton:
					        text: 'PUT'
					        icon: 'file-upload'
					        on_release:
					        	displaybox2.text="put response: "+app.menu.get(textbox2.text)
					    
					BoxLayout:
						orientation:"horizontal" 
						pos_hint: {"x":0,"y":.25}   
					    MDRectangleFlatIconButton:
					        text: 'HEAD'
					        icon: 'format-header-pound'
					        on_release:
					        	displaybox2.text="head response: "+app.menu.get(textbox2.text)
					        
					    MDRectangleFlatIconButton:
					        text: 'DELETE'
					        icon: 'delete'
					        on_release:
					        	displaybox2.text="delete response: "+app.menu.get(textbox2.text)

					    MDRectangleFlatIconButton:
					        text: 'OPTIONS'
					        icon: 'cloud-question'
					        on_release:
					        	displaybox2.text="options response: "+app.menu.get(textbox2.text)

				    MDRectangleFlatIconButton:
				        text: 'CLEAR'
				        icon: 'cancel'
				        color: 1,.1,.1,1
				        pos_hint: {"right":1,"y":0}
				        on_release:
				        	textbox2.text=""
				        	displaybox2.text="$"

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'About'
            icon: 'information'

            BoxLayout:
            	orientation:"vertical"
            	MDToolbar:
            		title: "About"
            		specific_text_color: 1,1,1,1

	            TextInput:
	            	text: """Fuck off..."""
	            	size_hint_y:None
	            	height:100
	            	disabled_foreground_color: 1,1,1,1
	            	border: 10,10,10,10
	            	background_color:1,1,1,0
	            	foreground_color:1,1,1,1
	            FloatLayout:

'''

class MenuScreen(Screen):
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
		try:
			r = requests.get("https://"+host)
			str_r = r.headers
			s_out =""
			resp = 0
			resp = r.status_code
			for key,value in str_r.items():
				s_out = s_out +str(key)+": "+str(value)+"\n"
		except requests.exceptions.RequestException as e:
			s_out = str(e)
		return s_out+"status code:"+str(resp)

	def post(self,host):
		try:
			r = requests.post("https://"+host)
			str_r = str(r.status_code)
		except requests.exceptions.RequestException as e:
			str_r = str(e)
		return str_r

	def post(self,host):
		try:
			r = requests.put("https://"+host)
			str_r = str(r.status_code)
		except requests.exceptions.RequestException as e:
			str_r = str(e)
		return str_r

	def head(self,host):
		try:
			r = requests.head("https://"+host)
			str_r = str(r.status_code)
		except requests.exceptions.RequestException as e:
			str_r = str(e)
		return str_r

	def delete(self,host):
		try:
			r = requests.delete("https://"+host)
			str_r = str(r.status_code)
		except requests.exceptions.RequestException as e:
			str_r = str(e)
		return str_r

	def options(self,host):
		try:
			r = requests.options("https://"+host)
			str_r = str(r.status_code)
		except requests.exceptions.RequestException as e:
			str_r = str(e)
		return str_r

#sm = ScreenManager()
#sm.add_widget(MenuScreen(name="menu"))



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'
        return  Builder.load_string(KV)

    menu = MenuScreen()
    

MainApp().run()