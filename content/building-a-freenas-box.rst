Building a FreeNAS Box
######################
:date: 2012-11-25 20:00
:author: Xitij Ritesh Patel
:category: Engineering
:tags: freenas, nas, projects

I've been having a lot of trouble lately trying to figure out the best solution for backing up my data. Recently, I've been accumulating a large number of files, photos, and videos that I'd like to keep safe. Moreover, I'd like this data to be accessible when needed. I have always thought that having a :abbr:`NAS (Network Attached Storage)` box would be one piece in solving that puzzle. The other would be some type of online backup solution, like BackBlaze that I recently signed up for through AppSumo. 

I haven't been able to properly evaluate BackBlaze yet, since I'm dealing with cleaning up my local data first before I start shuffling stuff into the cloud. However, it seems to be simple enough, and the price is right. The biggest issue seems to be uploading the data to them, since my upload bandwidth is contrained. Now might be the time to consider upgrading to Teksavvy's new DSL offerings.

With Black Friday just having passed, I set out to work on buying the parts for a FreeNAS machine. I wanted to do this last year, but was prevented by the high prices of hard drives. These seemed to have dropped back down to obtainable levels now. Below is the hardware I purchased.

- AMD A4-3400 Dual Core 2.70GHz APU - $49.99
- Gigabyte GA-A55M-DS2 Socket FM1 AMD A55 Chipset MB - $49.99 - $15 MIR
- Patriot Memory Viper 3 Mamba Black 8GB (2x4GB) RAM - $32.99 - $12 MIR
- Seagate Barracuda SATA3 1TB 32MB Cache HDD - $49.99 x 3
- Sub-total: $282.94
- Total (after taxes): $319.72
- Total (after MIRs): $292.72

I also bought a Kingston DataTraveller III 16GB USB stick for $9.99 to use as the boot disk for the FreeNAS box. However, after fighting with it for almost 3 hours to boot properly, I gave up and went with some free promotional USB stick. Suffice it to say, the Kingston sticks are being returned.

Once the box was assembled, I followed the instructions on the FreeNAS site to download and install it on the USB stick. Once I figured out the issues with my USB stick, things seemed to progress relatively smoothly. When the Kingston stick did boot, it would fail and fallback to the loader prompt (highlight by the ``mountroot>`` prompt). If you see this, just use another stick.

The included web GUI with FreeNAS is pretty decent. It lets you access most things you need to. I had to reboot a few times to deal with some issues with services not starting properly, but those are mostly resolved now. Coming from the Linux world, it's going to take some getting used to how things are done in the BSD world. Right now I've got a 1.8TB RAID-Z ZFS volume set up, with several datasets in place to store my documents, photos, and videos. Photos and videos are already copied over, now just working on my documents.

Once the copying is done, my hope is to put the FreeNAS box downstairs in the basement by my router, never to be seen again. I'll have a DLNA/UPnP media server set up on it to share videos and photos to the PS3 in my living room, as well as other PCs. Meanwhile, my intention is to have all my Bittorrent traffic handled by this box. I'll set up a script to automatically purge old downloads. I did have an idea to allow torrents to be added via e-mail or Dropbox. Another idea was to remotely search for torrents and have them download, since my fiancée frequently requests that I download shows for her. 

Oh and of course, once the data is properly backed up onto the FreeNAS box, I intend to have BackBlaze store everything in the cloud. I'll have to explore an option to use Amazon Glacier as well, to see if that saves me some money.

I'll update the blog with more articles as things progress.

