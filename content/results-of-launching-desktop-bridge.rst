Results of Launching Desktop Bridge
###################################
:date: 2012-06-12 14:17
:author: Xitij Ritesh Patel
:category: Ventures
:tags: blackberry, desktop bridge, PlayBook

.. youtube:: WZGaRTOsmn8

If you don't know what Desktop Bridge is, the YouTube video above should
help illustrate what it does.

Many of us have likely have had an idea similar to Desktop Bridge. I'm
sure many of you have thought that it would be great to access your
phone's functions from your PC, so you could respond to messages without
interrupting your workflow to pick up your device. I personally had the
idea ever since I first used a BlackBerry back in 2004 during my co-op
work term at RIM.

On the night of May 15, I thought I would just go for it and see if I
could create an app to make it happen. Over the course of 4 hours, I had
managed to write a proof-of-concept to demonstrate that it could work.
Within another 8 hours, I had the app working reliably with a usable UI.
After another 4 hours, I had the app ready to submit to App World on May
16. Like most developers, I figured App World approval would determine
whether or not RIM would sanction the app, which would ultimately
determine whether I should continue with my efforts. Over the course of
the next 2 weeks, I would quickly realize that I gave RIM too much
credit.

While I awaited approval, I continued to make my own refinements and
improvements. I figured that if RIM denied it, it would still be a very
useful app for my own personal use. It was at this point that I started
to understand some of the security implications of the app, namely the
fact that the PIM data was being transmitted wirelessly, without any
encryption or authentication. Thus, I started to come up with a solution
to this problem, working through a number of different options. I
eventually settled on using SSL-based encryption with a self-signed
certificate generated on the device. Moreover, every connection to the
app running on the PlayBook had to be confirmed via an on-screen
notification. I felt that this was a relatively good security solution
that balanced security with usability and simplicity.

On May 21, RIM approved Desktop Bridge for release. I was very excited,
and the approval simply added fuel to my efforts. I started thinking
about how to market and launch the app. I posted many screenshots to
twitter, and started engaging with potential customers and blogs. I
thought of ideas for the product page and a launch video. In fact, it
got plenty of other developers excited as well. I was able to get
preliminary access to `TestLab`_, which allowed me to coordinate the
release of 3 beta versions to a number of testers. I held off on posting
Desktop Bridge for sale because I wasn't happy with the security issues
surrounding the version I had submitted, and I wanted to coordinate the
launch to make it effective.

On May 23, I received another e-mail from BlackBerry App World notifying
me that Desktop Bridge was moved back to a 'Pending Review' state, and
that I would be notified once the extended review was complete. At this
point, I had no additional information or communications, so my
assumption was that they had the same security concerns that I did.
Shortly after receiving this e-mail, I uploaded one of my beta versions
to App World for their review, along with a changelog indicating that I
had added SSL-based encryption and device-side authentication. It was my
hope that it would demonstrate that I was continuing to work on Desktop
Bridge, and addressing any potential concerns they may have had.

I continued to work on the app, putting the final touches on it in
anticipation of launching it. I put up the product page, communicated
with various blogs, and continued sending tweets. I even contacted
`@BlackBerryDev`_ to find out if they had any information about what was
happening with the approval. Having a product move back into review was
quite unusual, and I was understandably concerned. `@BlackBerryDev`_ was
unable to provide any concrete details, but assured me that the review
was close to completion and that I should be receiving a decision soon.

Needless to say, I was quite nervous at this point. However, on Sunday,
May 27, Desktop Bridge was approved for release. I was floored, and in
disbelief. I contacted `@BlackBerryDev`_ asking if this approval was for
real. They said that if the App World team cleared it, then I should be
good to go. (In their defense, App World approvals are not their area,
they likely don't have much more information than me.)

I submitted one final version to App World for approval from their test
house, with all of the bugfixes I had implemented. This was to be my
launch version, and I was planning to launch at 9:00am on Tuesday, May
29, to catch the potential customers returning to work after the
Memorial Day weekend. I posted up a `countdown at Crackberry in their
forums`_, and tweeted about the launch date. I put together the final
edits on my launch video, uploaded it, and posted it just prior to
launch. I stayed up all night, too excited to sleep. At 9am, I posted it
for sale. At 11:30am, it was removed from App World.

Results of the Launch
---------------------

.. raw:: html
   :file: results-of-launching-desktop-bridge-map.html

For the short time that Desktop Bridge was in App World, I had 25 sales
in various countries in the $4.99 price tier. Moreover, I had `three
5-star reviews`_. After the app was pulled, I started receiving e-mails,
tweets, and even phone calls asking where Desktop Bridge went. This went
on for several days. I did my best to notify everyone of its removal,
but at this point, I decided to divert my attention to other things
while I collected myself and decided what to do next.

However, these results are still quite promising. They indicate the
potential success of Desktop Bridge, and how well it could have done if
RIM had not removed it from App World. It seems that my efforts would
have paid off.

In a small attempt to recoup some of my costs, I have decided to make
Desktop Bridge available to be sideloaded. If you want it for free,
here's a `link to the pirate site`_. If you'd like to buy it, you can
click the button below. I've lowered the price from $4.99 to $2, but
allowed you to name your own price as well. Please read the notes that
I've left on it, as I cannot guarantee future functionality.

.. raw:: html
   :file: desktop-bridge-gumroad.html

.. _TestLab: https://www.kisailabs.com/beta/
.. _@BlackBerryDev: https://twitter.com/#!/BlackBerryDev
.. _countdown at Crackberry in their forums: http://forums.crackberry.com/playbook-apps-games-f243/official-desktop-bridge-cb-thread-726633/
.. _three 5-star reviews: |filename|/images/ResultsDB_Reviews.jpg
.. _link to the pirate site: http://www.ipmart-forum.com/showthread.php?768293-Desktop-Bridge
