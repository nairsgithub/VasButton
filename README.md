VasButton Version 1

** Make Sure You Have Installed retrying and requests library installed if you dont have do pip install to install it

VasButtonTest.py is Beta Raspberry Pi compaitable software to start using VasButton on http://vastauine.com/vasbutton
Sign up for vastauine.com and then Download this file to your pi
modify Username and password field
DONE !
STEP by STEP Instruction :
** ASSUMING you have just unboxed your pi and are using a windows computer

Download Necessary Software : (you can download all of them from link here : http://blog.vastauine.com/vastauine/setup )
1.Raspbian-jessey OS
2.SD-card-formatter
4.Win-32Disk Imager
5.Putty

STEP 1: Insert your SD card to your computer Format it using SD-card Formatter and use Win-32Disk Imager to write Raspbian-jessey on your         SD card.

STEP 2 : Connect your Pi to computer using Putty
         power up your PI,connect pi to computer using Ethernet cable.
         open putty,enter your PI's ip Use port 22 and mark on SSH
         
STEP 3 : Connecting your Pi to Wifi
        * make sure you have your Wifi name and Password change it in the below code
        ** Go to this path copy paste following code make sure you cange your wifi ID and password field

-------------------------------------------------------------------------------------
>>sudo nano /etc/network/interfaces
--------------------------------------------------------------------------------------
         auto lo
         iface lo inet loopback
         
         auto eth0
         allow-hotplug eth0
         iface eth0 inet manual
         
         auto wlan0
         allow-hotplug wlan0
         iface wlan0 inet manual
         wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
         
         auto wlan1
         allow-hotplug wlan1
         iface wlan1 inet manual
         wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
----------------------------------------------------------------------------
>>sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
----------------------------------------------------------------------------
         ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
         update_config=1
         
         network={
                 ssid="WIFI-NAME"
         
                 psk="WIFI-PASS"
         
                 key_mgmt=WPA-PSK
         }

-----------------------------------------------------------------------------------------------------------------------------
reboot one using sudo reboot,make sure you are connected by doing ifconfig  if you are connected you can see a IP address in Wlan0

STEP 4: Download and vasbutton.py file on to your raspberry pi,(say u put it in directory /home/pi)

STEP 5: Set your PI to run vasbutton.py automatically every time you boot up!
Run following Command: sudo nano .bashrc
at the end of this file write command to run vasbutton.py : sudo python vasbutton.py

Now Restart your PI !

DONE !
>> Your home is Connected


