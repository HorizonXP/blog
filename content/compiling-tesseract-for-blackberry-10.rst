Compiling tesseract for BlackBerry 10
#####################################
:date: 2012-11-21 18:00
:author: Xitij Ritesh Patel
:category: Engineering
:tags: blackberry, ocr, coding

I've been on a hiatus from the blog for some time, so I figure I'll write something up that should be useful to a few people. 

Recently, I had an idea for an app, and part of it would utilize some :abbr:`OCR (Optical Character Recognition)` capabilities. Some quick Google searching revealed the `tesseract-ocr`_ library. Since it's a mature project, it seemed ripe for cross-compiling on BlackBerry 10. In fact, several people have done so for iOS and Android, giving me hope that it should be quite simple to accomplish. In fact, I used a blog post about `cross-compiling libraries for iOS`_ as a reference for my work.

Rather than detail my Herculean effort to get things going, I figure I'll just attach my modified scripts and steps to let you compile it. Most of the credit goes to Tinsuke Suzuki's `cross-compiling libraries for iOS`_ blog post. His steps create statically-linked libraries, which didn't fit my requirements. I made modifications to generated shared libraries. Also note that I ran this all on Ubuntu. If you're compiling on a different host OS, then... you're on your own!

#. Create a directory to house your source files. I put mine in ``~/build``.
#. Grab the latest `Leptonica sources`_ and save it to ``~/build``. I got version 1.69. 
#. Extract the source files with the following command:

   .. code-block:: sh

      tar -xvf leptonica-1.69.tar.gz
#. We need to fix some code in Leptonica that seems to fail at compile time. Not to worry, I've included a patch! Download this `patch for leptonica-1.69`_ to ``~/build`` and apply it using the following command:

   .. code-block:: sh

      patch -p1 -i leptonica-1.69.patch

#. Next, we need to grab the latest tesseract-ocr sources. 

   .. code-block:: sh

      svn checkout http://tesseract-ocr.googlecode.com/svn/trunk/ tesseract-ocr

#. We need to patch a couple of files here again. Download this `patch for tesseract-ocr`_ to ``~/build`` and apply it with the following command:

   .. code-block:: sh

      patch -p0 -i tesseract-ocr.patch

#. Make two more directories within ``~/build`` called ``dependencies`` and ``outdir``. 
#. Copy and paste the following into a file called ``build-dependencies.sh`` in ``~/build``.

   .. code-block:: sh
   
      GLOBAL_OUTDIR="`pwd`/dependencies"
      mkdir -p $GLOBAL_OUTDIR/include $GLOBAL_OUTDIR/lib
      OUTDIR="./outdir"
      LEPTON_LIB="`pwd`/leptonica-1.69"
      TESSERACT_LIB="`pwd`/tesseract-ocr"

      setenv_all()
      {
              source /opt/bbndk/bbndk-env.sh
              # Add internal libs
              export CFLAGS="$CFLAGS $MAKEFLAGS -I$GLOBAL_OUTDIR/include -L$GLOBAL_OUTDIR/lib"

              export CPP="$QNX_HOST/usr/bin/ntoarmv7-cpp-4.6.3"
              export CXX="$QNX_HOST/usr/bin/ntoarmv7-g++-4.6.3"
              export CXXCPP="$QNX_HOST/usr/bin/ntoarmv7-cpp-4.6.3"
              export CC="$QNX_HOST/usr/bin/ntoarmv7-gcc-4.6.3"
              export LD=$QNX_HOST/usr/bin/ntoarmv7-ld
              export AR=$QNX_HOST/usr/bin/ntoarmv7-ar
              export AS=$QNX_HOST/usr/bin/ntoarmv7-as
              export NM=$QNX_HOST/usr/bin/ntoarmv7-nm
              export RANLIB=$QNX_HOST/usr/bin/ntoarmv7-ranlib
              export LDFLAGS="-L$QNX_TARGET/armle-v7/usr/lib/"

              export CPPFLAGS=$CFLAGS
              export CXXFLAGS=$CFLAGS
      }

      setenv_arm7()
      {
              setenv_all
      }

      #######################
      # LEPTONLIB
      #######################
      cd $LEPTON_LIB
      rm -rf $OUTDIR
      mkdir -p $OUTDIR/arm7

      make clean 2> /dev/null
      make distclean 2> /dev/null
      setenv_arm7
      ./configure --host=arm-qnx --enable-shared=yes --disable-programs --without-zlib --without-libpng --without-jpeg --without-giflib --without-libtiff
      make -j4
      cp -rvf src/.libs/lib*.so $OUTDIR/arm7
      cp -rvf src/.libs/lib*.so.3 $OUTDIR/arm7
      cp -rvf src/.libs/lib*.la $OUTDIR/arm7

      mkdir -p $GLOBAL_OUTDIR/include/leptonica && cp -rvf src/*.h $GLOBAL_OUTDIR/include/leptonica
      mkdir -p $GLOBAL_OUTDIR/lib && cp -rvf $OUTDIR/arm7/lib*.so $GLOBAL_OUTDIR/lib
      cp -rvf $OUTDIR/arm7/lib*.so.3 $GLOBAL_OUTDIR/lib
      cp -rvf $OUTDIR/arm7/lib*.la $GLOBAL_OUTDIR/lib
      cd -

      #######################
      # TESSERACT-OCR (v3)
      #######################
      cd $TESSERACT_LIB
      rm -rf $OUTDIR
      mkdir -p $OUTDIR/arm7

      make clean 2> /dev/null
      make distclean 2> /dev/null
      setenv_arm7
      bash autogen.sh
      ./configure --host=arm-qnx --enable-shared=yes --without-libtiff LIBLEPT_HEADERSDIR=$GLOBAL_OUTDIR/include/
      make -j4
      for i in `find . -name "lib*.so"`; do cp -rvf $i $OUTDIR/arm7; done
      for i in `find . -name "lib*.so.3"`; do cp -rvf $i $OUTDIR/arm7; done
      for i in `find . -name "lib*.la"`; do cp -rvf $i $OUTDIR/arm7; done

      mkdir -p $GLOBAL_OUTDIR/include/tesseract && cp -rvf api/apitypes.h api/baseapi.h ccmain/thresholder.h ccstruct/publictypes.h ccutil/ocrclass.h ccutil/unichar.h $GLOBAL_OUTDIR/include/tesseract
      mkdir -p $GLOBAL_OUTDIR/lib && cp -rvf $OUTDIR/arm7/lib*.so $GLOBAL_OUTDIR/lib
      cp -rvf $OUTDIR/arm7/lib*.so.3 $GLOBAL_OUTDIR/lib
      cp -rvf $OUTDIR/arm7/lib*.la $GLOBAL_OUTDIR/lib
      cd -


#. Now that all the pieces are in place, you can execute the ``build-dependencies.sh`` script as follows:

   .. code-block:: sh

      chmod +x build-dependencies.sh
      ./build-dependencies.sh

Let that run for a few minutes. Once complete, you should have everything you need in the dependencies folder to start using tesseract-ocr in your BlackBerry 10 applications.

If you found this useful, let me know! Would love to hear about the applications you're building and how I can help.

.. _tesseract-ocr: http://code.google.com/p/tesseract-ocr/
.. _cross-compiling libraries for iOS: http://tinsuke.wordpress.com/2011/02/17/how-to-cross-compiling-libraries-for-ios-armv6armv7i386/
.. _Leptonica sources: http://www.leptonica.com/download.html
.. _patch for leptonica-1.69: other_files/leptonica-1.69.patch
.. _patch for tesseract-ocr: other_files/tesseract-ocr.patch
