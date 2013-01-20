How to Implement Pull to Refresh in BlackBerry 10 Cascades
##########################################################
:date: 2013-01-20 16:30
:author: Xitij Ritesh Patel
:category: Engineering
:tags: blackberry 10, cascades, blackberry-py, sample

.. image:: |filename|/images/CascadesPullToRefreshSample.jpg
   :width: 100 %

Over the last little bit, I've been doing a lot of work on some apps for
BlackBerry 10.  `With January 30th fast approaching`_, I was coding like
a madman to try and meet the deadline, so I can get my hands on some awesome
swag.

I was able to pump out two good quality apps relatively quickly by using the
Tart project from the `blackberry-py project`_.  Thanks to `Peter Hansen
(@peter9477)`_, we can write entire apps using just Python, QML, and JavaScript
that perform at near-native speeds.  This workflow allows you to rapidly
prototype your app, far outweighing any concerns about performance when
compared to C++. 

One of the apps I built uses a UI paradigm called "Pull to Refresh."  If the
user is viewing a stream of data, they can pull down on the list and reveal
a hidden item that notifies them they can refresh the stream contents by
releasing their touch.  A number of people have asked me how to implement this.  

Again, because of the speed of development that's possible with BB Tart, I was
able to put together a crude, but workable sample demonstrating how to
implement this feature.  Furthermore, I even integrated it with `ADN's global
feed`_.  I simply pulled a couple of libraries from Github and putting the
building blocks together.  I went from idea to functioning sample in 12 hours,
with 6 hours of sleep in between. 


As you can see, everything you need is in the `blackberry-py-pulltorefresh`_
GitHub repo.  The app was built on top of my `blackberry-py-bootstrap`_ repo.
I'd be more than willing to accept help/pull requests on the project to help
improve it for all developers.  The file you should look at in particular is
``PullToRefresh.qml``.

.. raw:: html

    <script
    src="http://gist-it.sudarmuthu.com/https://github.com/HorizonXP/blackberry-py-pulltorefresh/blob/master/assets/PullToRefresh.qml?footer=minimal&slice=28:-1"></script>

You'll note that I implemented a `LayoutUpdateHandler`_ to monitor changes in
the item.  If the Y-coordinate is equal to exactly 0, then it fires the
``refreshTriggered()`` signal.  In my testing, this works relatively well since
the control will snap to 0 when it is released past the threshold.  However, it
can sometimes be triggered while the user is still interacting with the
control.  Therefore, a better way would be to detect if the user is touching
the control, and only firing if they're not.  

I hope that helps most of you BlackBerry 10 developers looking to implement
this in your app.  When I first got this working, I couldn't stop playing with
it!  Hopefully this gives you the jumpstart you need.  Oh and take a look
through the rest of the repository, there's some good stuff in there including
a way to asynchronously load remote images. 

.. raw:: html

    <div id="repo"></div>
    <script>
    jQuery(function($){
      $('pre').vanGogh();
      $('#repo').repo({ user: 'HorizonXP', name: 'blackberry-py-pulltorefresh' });
    });
    </script>


.. _With January 30th fast approaching: http://blogs.blackberry.com/2012/11/blackberry-10-launch-event/
.. _blackberry-py project: http://blackberry-py.microcode.ca/
.. _Peter Hansen (@peter9477): http://peterhansen.ca/blog/
.. _ADN's global feed: https://alpha.app.net/global/
.. _blackberry-py-pulltorefresh: https://github.com/HorizonXP/blackberry-py-pulltorefresh
.. _blackberry-py-bootstrap: https://github.com/HorizonXP/blackberry-py-bootstrap
.. _LayoutUpdateHandler: https://developer.blackberry.com/cascades/reference/bb__cascades__layoutupdatehandler.html
