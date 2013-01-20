Google Chromebook and Ubuntu
#############################
:date: 2012-12-16 08:00
:author: Xitij Ritesh Patel
:category: Engineering
:tags: ubuntu, chromebook

I got my Google ARM Chromebook! 

.. image:: |filename|/images/Google-Chromebook.jpg
   :width: 100 %

I was really excited for this device. I've been using a thick, heavy, and
relatively underpowered Acer laptop for the last 5 years. I really wanted
something thin and light to do my development work on that I could use on the
go. This meant moderate power with ample battery life.

The ARM-based Google Chromebook wouldn't seem the fit the bill, if only for the
fact that it uses a custom Chrome OS. However, a Googler named Olof Johansson
`put up some instructions`_ detailing how you might install Ubuntu onto an SD
card. 

His instructions worked relatively well, but I would like to supplement it.
Olof used rootstock to create his SD card's root filesystem. I opted to
download the ``ubuntu-core`` tarball instead from the `Quantal Quatzal`_ repo.
Continuing with his instructions, I was able to get Ubuntu up and running with
the terminal. However, I couldn't install packages because I didn't have
Internet access. A little bit of troubleshooting led me to 2 possibilities for
connectivity: a) wireless b) wired via a USB-to-Ethernet adapter. I don't have
an adapter available, and didn't want to buy one. Thus, I tried to figure out
what I needed to do get wireless working.

Thankfully, Olof's instructions made sure that we have the wireless module
available and loaded, so that reduced a lot of my effort. What I did forget to
do was add a user to the Ubuntu installation. I found the easiest way to
accomplish this was to mount the SD card in the Chrome OS terminal, chroot to
it, and add the user. Make sure to give that user sudo access by adding it to
the ``adm`` and ``sudo`` groups.

After a bunch of trial and error, I found that I needed the following packages
to get wireless working sufficiently to allow me to install a desktop
environment. I've included direct links to the package.

Packages to Install:

========================================== ======================
Name                                       URL
========================================== ======================
isc-dhcp-common_4.2.4-1ubuntu10_armhf.deb  http://ports.ubuntu.com/pool/main/i/isc-dhcp/isc-dhcp-common_4.2.4-1ubuntu10_armhf.deb
isc-dhcp-client-4.2.4-1ubuntu10_armhf.deb  http://ports.ubuntu.com/pool/main/i/isc-dhcp/isc-dhcp-client-4.2.4-1ubuntu10_armhf.deb
wpasupplicant_1.0-2ubuntu5_armhf.deb       http://ports.ubuntu.com/pool/main/w/wpa/wpasupplicant_1.0-2ubuntu5_armhf.deb
libpcsclite1_1.8.5-1ubuntu1_armhf.deb      http://ports.ubuntu.com/pool/main/p/pcsc-lite/libpcsclite1_1.8.5-1ubuntu1_armhf.deb
net-tools_1.60-24.1ubuntu3_armhf.deb       http://ports.ubuntu.com/pool/main/n/net-tools/net-tools_1.60-24.1ubuntu3_armhf.deb       
iw_3.4.1_armhf.deb                         http://ports.ubuntu.com/pool/main/i/iw/iw_3.4.1_armhf.deb                         
crda_1.1.2-1ubuntu2_armhf.deb              http://ports.ubuntu.com/pool/main/c/crda/crda_1.1.2-1ubuntu2_armhf.deb              
wireless-regdb_2011.04.28-1ubuntu3_all.deb http://ports.ubuntu.com/pool/main/w/wireless-regdb/wireless-regdb_2011.04.28-1ubuntu3_all.deb 
libnl-genl-3-200_3.2.7-4_armhf.deb         http://ports.ubuntu.com/pool/main/libn/libnl3/libnl-genl-3-200_3.2.7-4_armhf.deb         
libnl-3-200_3.2.7-4_armhf.deb              http://ports.ubuntu.com/pool/main/libn/libnl3/libnl-3-200_3.2.7-4_armhf.deb              
libssl1.0.0_1.0.1c-3ubuntu2_armhf.deb      http://ports.ubuntu.com/pool/main/o/openssl/libssl1.0.0_1.0.1c-3ubuntu2_armhf.deb      
sudo_1.8.5p2-1ubuntu1_armhf.deb            http://ports.ubuntu.com/pool/main/s/sudo/sudo_1.8.5p2-1ubuntu1_armhf.deb            
========================================== ======================


You can download those packages and put them into ``/var/cache/apt/archives``
to ensure that ``apt-get`` will find them. Go ahead and boot into Ubuntu, then
install those packages. You should have everything you need to connect to
a wireless network and complete installing the rest of Ubuntu. 

A word of warning: I couldn't get ``ubuntu-desktop`` working with Unity. That's
even with using the packages from the `Chromebook-ARM Launchpad`_ project. The
first problem was the lack of ``/etc/X11/xorg.conf.d/exynos.conf`` on the SD
card; I simply copied this from the Chrome OS partition. After this, whenever
I booted into Unity, I would only have the desktop background. For this reason,
I would recommend avoiding Unity, and install ``xubuntu-desktop`` instead. 

So far, I'm pretty happy with this setup, especially when tied with my Amazon
EC2 instance. There are still several deficiencies, such as a good keyboard
map, a properly working touchpad, and graphics acceleration. Power management
and hibernation support would be nice too. I suppose these are things that will
be ported over. I might put some time into doing that myself.

Finally, ARM support for some key programs aren't there. I can't get the
Dropbox client working, nor could I get an Adobe Flash plugin working for
Chromium. Hopefully the upstream maintainers will release ARM versions. 

.. _put up some instructions: https://plus.google.com/109993695638569781190/posts/b2fazijJppZ
.. _Quantal Quatzal: http://cdimage.ubuntu.com/ubuntu-core/releases/12.10/release/ubuntu-core-12.10-core-armhf.tar.gz
.. _Chromebook-ARM LaunchPad: https://launchpad.net/chromebook-arm
