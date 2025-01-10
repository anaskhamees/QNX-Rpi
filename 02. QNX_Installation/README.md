# QNX Academic Version (Non-Commercial)
### 1. QNX Installation

**1.1. Create Your QNX Account from [HERE](https://www.qnx.com/account/login.html?logout=1#showcreate) Then Activate your QNX Account** 

**1.2. Request Free QNX License from [HERE](https://qnx.com/getqnx)** 

**Please follow This Video**  :

https://www.youtube.com/watch?v=DtWA5E-cFCo&t=313s

- **After requesting , If you go to License Manager [HERE](https://www.qnx.com/account/dashboard/)** 

![image-20241226005315716](README.assets/image-20241226005315716.png)

- **You should accept the license and deploy it on your QNX Account [See the above video]**

![image-20241226010123632](README.assets/image-20241226010123632.png)



- **If you go to the registered products in your QNX profile :**

![image-20241226010807324](README.assets/image-20241226010807324.png)

- **Go to the QNX Software Center to download QNX**

![image-20241226011112709](README.assets/image-20241226011112709.png)

- **I use Linux Ubuntu 22.04 LTS, So I will select Linux Host**

- **To install the QNX Software Center on a Linux development host:**

  - Log in to your **myQNX** account on the QNX website, select the Developers tab at the top of the page, then click the QNX Software Center link.

  - Click the link for Linux hosts and download the QNX Software Center installer, 

    `qnx-setup-*nnnnnnnnnnnn*-lin.run` , where *nnnnnnnnnnnn* is a build number.

    ![image-20241226012550394](README.assets/image-20241226012550394.png)

  - To ensure you are running the official installer, verify that the checksum of the downloaded file matches the checksum posted on the QNX website. (This step is required because Linux doesn't support automatic verification of binary signatures.)

![image-20241226014338025](README.assets/image-20241226014338025.png)

- **Run `chmod` to make the installer executable**

```bash
chmod a+x qnx-setup-2.0.3-202408131717-linux.run
```

**1.3. Install Software Development Platform SDP , Version QNX 8.0 for Linux**

- **Run the installer**

  ```bash
  ./qnx-setup-2.0.3-202408131717-linux.run
  ```

![image-20241226015938816](README.assets/image-20241226015938816.png)

![image-20241226020325093](README.assets/image-20241226020325093.png)

- **Add Installation**

![image-20241226020904724](README.assets/image-20241226020904724.png)

- **Select QNX SDP 8.0** then Click Next  :

  ![image-20241226021313708](README.assets/image-20241226021313708.png)

![image-20241226021420499](README.assets/image-20241226021420499.png)

![image-20241226021516560](README.assets/image-20241226021516560.png)

![image-20241226021554280](README.assets/image-20241226021554280.png)

![image-20241226021620899](README.assets/image-20241226021620899.png)

![image-20241226021640730](README.assets/image-20241226021640730.png)

- **Then Press Finish**

![image-20241226021732674](README.assets/image-20241226021732674.png)

![image-20241226021915396](README.assets/image-20241226021915396.png)

![image-20241226023520759](README.assets/image-20241226023520759.png)

- **After Installation DONE **

  ![image-20241226024030630](README.assets/image-20241226024030630.png)



![](README.assets/image-20241226024217065.png)

![image-20241226024348765](README.assets/image-20241226024348765.png)

>Software Development Platform (SDP) Version 8.0 of the QNX Software Center installed in **qnx800** directory.  

![image-20241226024933701](README.assets/image-20241226024933701.png)

>The **host** folder is where you will find the tools necessary for building programs on your computer, while the **target** folder contains all of the files that can go on your QNX system (though you will only ever likely need a small subset of these).



To develop Apps on QNX for a particular board, you will need to add the relevant board support package **(BSP)**, which contains the source code and binaries for the specific hardware [in my case **RPI-4**]. 

The SDP provides everything you need in order to build your own QNX system. How-ever, to get you up and running quickly with Raspberry Pi, we will use a pre-defined image that you can just copy to an SD card. 

**1.4. Install QNX SDP 8.0  Image for Raspberry Pi 4** [2,4,8 G RAM only] 

Open QNX Software Center, and install the **“QNX® SDP 8.0 Quick Start image for Raspberry Pi 4”** package.

- **Open QNX Software Center** :

   `Updates -> QNX Software Development Platform -> Reference Images:`

![image-20241226035710844](README.assets/image-20241226035710844.png)

![image-20241226040412181](README.assets/image-20241226040412181.png)

**Then Press Install**

![image-20241226040458924](README.assets/image-20241226040458924.png)

![image-20241226040540907](README.assets/image-20241226040540907.png)

- **After Rpi4 Image Installed** :

![image-20241226041650782](README.assets/image-20241226041650782.png)

- **When Open qnx800 directory again there is new directory called `images`**

![image-20241226042002564](README.assets/image-20241226042002564.png)

![image-20241226042126589](README.assets/image-20241226042126589.png)

```bash
ls -lh qnx_sdp8.0_rpi4_quickstart_20241216.img
du -h qnx_sdp8.0_rpi4_quickstart_20241216.img 
```

------------------------------------------------------

#### 2. Flash QNX SDP 8.0  Image  for Rpi4 on SD Card

There are two utilities to flash images on SD cards [or any removable device]

**2.1. Raspberry Pi Imager [Option#1]**

![image-20241226044745549](README.assets/image-20241226044745549.png)

- `Operating System ` : choose your Image
- `Storage` : choose your removable device [e.g. SD card]

![image-20241226052820290](README.assets/image-20241226052820290.png)

![image-20241226053621290](README.assets/image-20241226053621290.png)

**2.2. Linux Command Line `dd`  [Option#2]**

```bash
dd if=<Your_Image> of=<device name> bs=4M status=progress
```

- To Know the device name, open the terminal and run : 

  ```bash
  lsblk
  ```

  ![image-20241226054025755](README.assets/image-20241226054025755.png)

In my case the SD card [device name] is `sdc`

```bash
dd if=qnx_sdp8.0_rpi4_quickstart_20241216.img of=/dev/sdc bs=4M status=progress
```

![image-20241226054349930](README.assets/image-20241226054349930.png)

![image-20241226061108270](README.assets/image-20241226061108270.png)

--------------------

Once the image has been copied to the SD card and remains connected to your computer, you should be able to view the files written to the first partition (a FAT partition accessible by any operating system). Within this partition, two files require editing to configure the system:

- The first file, **qnx_config.txt**, does not need modification unless you want to adjust the default hostname (currently **qnxpi**) or specify the destination for console output.

  ![image-20241228022729345](README.assets/image-20241228022729345.png)



- The second file that requires updating is **wpa_supplicant.conf**. At the bottom of this file (following extensive documentation), you’ll find the **network settings** configuration section. Modify the `ssid` field to match your WiFi network name and the `psk` field to your WiFi password. These configurations assume a typical home network using WPA authentication.

  ![image-20241228023307691](README.assets/image-20241228023307691.png)

### 3. Booting the Raspberry Pi 4 

- Unplug the SD card from computer and connect it to RPI4.

- Connect HDMI display, micro-HDMI connector and a USB keyboard Only required
  if you want to connect to the system with a keyboard and a display.

- I use Rpi Touch Screen 7 inch

- Connect keyboard and mouse to play with the system.

  ![image-20250110180920744](README.assets/image-20250110180920744.png)

- USB-TTL converter Only required for troubleshooting the system over a serial
  console.

#### 3.1. Welcome Screen

- The following screen will appears after RPI4 booting , Press the power icon to open the terminal

![qnxWelcome](README.assets/qnxWelcome.jpeg)

- QNX Terminal 

  ![qnxTerminal](README.assets/qnxTerminal.jpeg)

I login in the first time using :

- **login username: root**
- **password : root**

>If **root** did not work. You can log in as either **qnxuser** or **root** and execute shell
>commands.

After you login successfully , the following terminal will appear

![loginqnx](README.assets/loginqnx.jpeg)

#### 3.2. Let's navigate to QNX rpi system

- QNX-RPI root file system

  ![qnxrootfs](README.assets/qnxrootfs.jpeg)

- QNX-RPI users

  ![qnxusers](README.assets/qnxusers.jpeg)

> I will use **qnxuser** as qnxpi user because **root access over SSH is disabled by default. **
>
> ![image-20250110220054673](README.assets/image-20250110220054673.png)
>
> So, Make sure you update these passwords [**password of qnxuser**] the first time you log in. Passwords can be changed using the **passwd** shell command. 

- Make password for `qnxuser` user 

  ```bash
  passwd qnxuser
  ```

  

![passqnx](README.assets/passqnx.jpeg)



### 4. SSH Connection between computer (host machine) and QNX-RPI (target machine)

- open the terminal on host machine (computer)

  ```bash
  ssh qnxuser@qnxpi.local
  ```

  ![image-20250110220558808](README.assets/image-20250110220558808.png)



>**How `qnxpi.local` Works** :
>
>1. **Hostname Configuration on QNX RPI**:
>   - The hostname `qnxpi` is set in the file `qnx_config.txt` on the Raspberry Pi's SD card.
>   - By default, the full name becomes `qnxpi.local` for mDNS.
>2. **mDNS Advertisement**:
>   - The QNX system runs a service (similar to `avahi-daemon` on Linux or `Bonjour` on macOS/Windows) that broadcasts its hostname (`qnxpi.local`) and IP address to other devices on the same local network.
>3. **Your Ubuntu System Resolves the Name**:
>   - If `avahi-daemon` or a similar mDNS service is running on your Ubuntu system, it listens for mDNS advertisements and maps `qnxpi.local` to the advertised IP address.
>   - This allows you to refer to the RPI by `qnxpi.local` without knowing its actual IP address.

![image-20250110220813284](README.assets/image-20250110220813284.png)

Now, I have the full control of the QNX on RPI target from my host computer
