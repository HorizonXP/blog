Why I Like BlackBerry 10 and Why I Don't Hate iOS/Android
#########################################################
:date: 2012-11-27 23:00
:author: Xitij Ritesh Patel
:category: Engineering
:tags: blackberry, iOS, Android, development, hacks

Some of you may know that I do quite a bit of development work. I've consulted on a number of projects through my company `Pulsecode`_ and more recently, I've worked on bootstrapping my own startup, `taab`_. In my endeavours, I've been exposed to a number of platforms, the most recent being BlackBerry 10. In fact, I built `taab`_'s prototype on BlackBerry 10 first, which I `detailed in this blog post`_. If you haven't read that post, you should since it provides an overview of what makes QNX and BlackBerry 10 so great. It was relatively well-received.

I make it no secret that I want BlackBerry 10 to succeed. I still cling to my BlackBerry Bold 9900, even though it makes me frustrated at times, and despite the fact that I actually own a Galaxy Nexus, Nexus 7, and have 3 iPhones in my household. While you may accuse me of being biased, you can't accuse me of being ignorant or a blind fan. 

Why BlackBerry 10?
------------------

Development on BlackBerry 10 is leagues better than what was available on legacy BlackBerry, and dare I say, even better than Android. Similar to Android's :abbr:`ADT (Android Development Tools)` plugin for Eclipse, BlackBerry 10's QNX Momentics :abbr:`IDE (Integrated Development Environment)` is Eclipse-based. It provides much of the same debugging power, but with key differences. While it is possible to debug and deploy to an Android device wirelessly, it isn't officially supported, so getting it to work is a bit of a pain. QNX Momentics allows a developer to deploy and debug to a device via WiFi or :abbr:`USB (Universal Serial Bus)`. This may seem like a small detail, but it definitely helps speed up the workflow. 

Moreover, as I outlined in my `previous writings`_, you don't hae to use QNX Momentics if you don't want to. In fact, I don't at all. You can perform all your development and debugging from the command line with the provided tools in the SDK. If you're already familiar with the GNU toolchain, then you will have no problems adapting your workflow. 

One of the things I learned while writing an Android app for a client (I should do a case study about this), is that the Android emulators *suck*. You can debate all you want about developing on a simulator vs. an emulator, but the fact that Android developers have put up with this for so long baffles me. I know that there is an Intel-based emulator in place, but how long has that taken? Fact is, :abbr:`RIM (Research in Motion)` makes VMWare images for its simulators available with every :abbr:`SDK (Software Development Kit)` release. And since it actually performs well, I can actually get work done with it.

Finally, BlackBerry 10 lets me develop directly on the metal with C/C++. Moreover, I can leverage Qt to help me ensure that my app is written using well-reviewed libraries. I don't have to deal with garbage collector issues, and I can focus on making my app work. Sure, I still have to be careful about the code that I write, but at least I'm in control of what happens, not the :abbr:`VM (Virtual Machine)` or :abbr:`OS (Operating System)`. 

Why Don't I Hate iOS/Android?
-----------------------------

Despite the issues I have with Android's development environment, I don't hate it. Sure, there are issues plaguing it, but despite that, many developers have created compelling apps using it. Indeed, Google Play is unarguably the most open app marketplace, and Android users and developers are afforded a great deal of freedom. However, I would argue the development environment and the difficulties associated with it are part of the reasons why the apps aren't always of the greatest quality. Moreover, the high learning curve is likely why most apps appear on the iTunes App Store before Google Play. It was true for the client I worked for.

I cannot say anything bad about Apple, iOS, or XCode, since it's not a development environment I have experience with. I'm working to rectify this in the near future (I'm on the hunt for a cheap Mac Mini). 

But I don't hate either platforms. When apps are done well, they're *gorgeous* on both, and they both have compelling features and capabilities. We can attribute the rapid growth of the smartphone market to Apple, since they gave everyone (including :abbr:`RIM (Research in Motion)`) a swift kick in the ass. Google is taking it to the masses with Android.

Fact is, I'm not comfortable using an iOS device or an Android device. To me, it feels clunky, even in comparison to my BlackBerry Bold 9900. It's no contest that BlackBerry 10 fits me even better. I'm a BlackBerry person.

But I don't belittle or berate others for their choice in smartphone. A phone is a very personal thing, and you need to choose what fits your usage scenario the best. For some it's an iPhone, for others it's an Android device. Honestly, with the capabilities of smartphones today, you *cannot* go wrong with any choice. They're all fantastic, and pack a lot of power. Actually, you can go wrong by choosing a non-Nexus Android device. How people deal with anything other than vanilla Android just baffles me. 

Sentiments Towards BlackBerry 10
--------------------------------

If you've been watching :abbr:`RIM (Research in Motion)`'s stock price lately, you'll see that they've been rallying in the last few weeks. Indeed, market sentiment seems to be shifting to their favour, as many media outlets and carriers are giving positive reviews of BlackBerry 10. 

Some developers have been giving it praise as well. Harry Kalogirou wrote about porting his iOS game, Pop Corny to the BlackBerry PlayBook, and how `he was impressed with it`_. Nathan Campos recently wrote about how `RIM is doing it right`_  and was promptly lambasted by people in the comments for his decision to develop for BlackBerry 10. These are two developers that have previous groundings in iOS, yet were sufficiently impressed by BlackBerry 10 to make the switch *before launch.*

So to those saying that BlackBerry 10 is dead in the water, that being 3rd place isn't good enough, and that no one will switch now that they're entrenched in iOS or Android, I humbly disagree. It's true, the BlackBerry die-hards will upgrade immediately. There will be folks that migrated to other platforms from BlackBerry, that want to come back and will. These are the BlackBerry people that :abbr:`RIM (Research in Motion)` is targeting. However, slowly but sure, folks will be drawn to BlackBerry 10. It won't be a blockbuster launch like Apple likes to do, it will be slow and gradual. Ultimately though, RIM has fixed and leap-frogged the developer ecosystem issues that had plagued it before. The new :abbr:`OS (Operating System)` is awesome. They've got a winner on their hands. But it will boil down to their marketing. And that's why I'm hopeful, but cautiously optimistic.

One final note: I'm working on an app for BlackBerry 10 that I'm hoping will let me serve an underserved niche market that has been neglected by a lot of developers. Of course, in true entrepreneurial spirit, I hope to monetize as well. I've teamed up with a designer named `Michael Buck`_ who has done some pretty awesome work on iOS apps. Today, he was one of 5 people to obtain a Dev Alpha device during a mini BlackBerry Jam event in Hamburg. All because of this video he put together below. He's awesome, you should check him out.

.. raw:: html

   <iframe src="http://player.vimeo.com/video/54298069?badge=0" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe> <p><a href="http://vimeo.com/54298069">BB-JAM - Icon-Test</a> from <a href="http://vimeo.com/iammichaelbuck">Michael Buck</a> on <a href="http://vimeo.com">Vimeo</a>.</p>

.. _Pulsecode: http://pulsecode.ca
.. _taab: http://taab.co
.. _detailed in this blog post: http://blog.taab.co/2012/08/15/how-were-building-taab-for-blackberry-10/
.. _previous writings: http://blog.taab.co/2012/08/15/how-were-building-taab-for-blackberry-10/
.. _he was impressed with it: http://kalogirou.net/2012/08/25/impressed-by-the-new-blackberry-os-or-how-ios-ate-dust/
.. _RIM is doing it right: http://nathancampos.me/post/30259200001/rim-is-doing-it-right
.. _Michael Buck: http://dribbble.com/MichaelBuck
