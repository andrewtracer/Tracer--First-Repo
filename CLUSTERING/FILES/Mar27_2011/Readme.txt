Aligned spectrometer:  a4 and checked wavelength
March 27, 2011, 12pm
L011711 substrate we measured last time, now patterned.  Film cracked due to vacuum/photoresist.

h k l  tth    th     chi     phi
0 0 1  35.125 19.694 87.265 .001
1 0 0  35.125 17.563 -4.125 36.206

went to hhl zone,
adjusted slits

There is a shoulder in this film on the 111 reflection:  see fpx03006.bt9

mesha 30 sec/pt
1-26  ack!  one peak?  upside down?  (killed 26 early)

rotate phi by 180 degrees and set 24=0 there.
Turns out that setting a24 is not enough for virtual motors, so at 180, we will initialize a24=0
but even this would be too easy, so for a25=90, a24=0 (software), but a24=7.5 hardware, so we'll have to live with it...
ack!  Even this doesn't work, have to have a25=0 and reinitialize phi=0 (when it's really 180 there...)
Next, reset ub matrix
(note the shoulder in fpx03008)
001  35.125 14.806 91.874 0.001 (remember that we set 180=0 for a24)
100  35.125 17.563 2.269 36.278

meshb*
hscan001 
.5 .5 .5
l=.5, .492, .488
hscan002 (scan along 11 -1) Only see one peak.

meshc* .485 .485 -.5 try a couple of scans
-.5, -.488,-.502, .-492
--------------

Ack!  move phi=90, init to 0
try again
centering steps:
001  mv phi="0", mv chi=90, mv th to tth/2, scan
optimize th, chi, th again record
100 mv th=tth/2, mv chi=0, find phi (make sure it is to the "right", so we are consistent) and phi
optimize phi, chi, record
move to 111 in hhl zone
opimize th, chi, phi, th, set3=angle from buf 1
mesh scan


    tth th chi phi
001 35.125 14.871 87.329 .001
100 35.125 17.563 -1.537 36.272

aligned on .5 .5 .5
meshd* .5, .502, .496,.504,.508
hscan*003 .492 .492 .5 scan along 1 1 -1  => 1 peak
hsca*004 .492 .492 .5 scan along 1 1 0=> 1 peak
hs*005 .492 .492 .5 scan along 0 0 1 two peaks?
hs*006 .492 .492 .5 scan along 1 1 1--> one peak

-------

Last chance, 
we've tried normal, 180 degrees (and hh-l), 90 degree
Now, try 270 and then we're done. (set phi=0 at 270)
found 001 and 100
      tth    th    chi    phi   
001 35.125 19.155 92.101 0.002
100 35.125 17.563 -0.274 36.247
aligned on 111 peak in hhl zone
 
meshe*
hscan007 .496 .496 .502 scan along 1 1 -1 one peak
hs*008 .496 .496 .502 scan along 1 1 0 one peak
hs*009 .496 .496 .502 scan along 1 1 1 one peak

----
Give up in abject failure
-----

Next film:
L011111 from 11th January 2011

started with a configuration

see fpx03028 for 001 reflection mosaic

    tth th chi phi
001 35.125 14.780 84.319 0.001
100 35.125 17.563 -5.891 3.491

check fpx03030 on 111 reflection:  mosaic or statistics?

meshf*1-25  (ignore later ones)
hscan010 a brief attempt to find more than one peak...fail.....

we go to the hkk zone.set a3 to hardware value.go back 100 peak.
optimize chi,phi,th for 100 peak
      tth    th    chi    phi   
100 35.125 17.563 -6.027 3.749
001 35.125 19.155 92.101 0.002

found 111 peak in the hkk zone
      tth    th      chi    phi   
111 63.020 -11.214 46.639  98.263

ignore these, went back to original matrix,
went to hkk zone, optimized 111 reflection (rather off in a3 --by 7 degrees....strange...)

meshg*
1-19 bad (19 terminated early)

hkl tth th chi phi
111 63.016 16.652 42.804 91.644

so, ignore meshg as well... checked and found that a3 was set wrong
meshh* ignore, somehow orient1 and orient2 were swapped
meshi* one peak
hscan011 looks like 1 peak

----
rotate phi 90 =>0 and try again

001 35.125 11.751 91.658 .001
100 35.125 17.563 1.347 3.134

meshj* it's a blob
hscan012 looks like one peak, but off center
hscan013 .493 .493 .485 almost double the counting time, one peak and shoulder?
remember this zone...
chi=49.524, phi=91.485 (after the original phi rotation by 90)

% pa
 Soft: A01=  20.589  A02=  41.177  A03=  52.289  A04=  30.380  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03= -15.803  A04=  30.438  A05=  20.831
 Soft: A06=  41.179  A07=  87.358  A08=  49.524  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=  87.358  A08=  49.524  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24=  91.485  A25=  49.524
 Hard: A24=  91.485  A25=  49.524


% dq 1,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
pa
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -1.320  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07=  87.358  A08=  49.524  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=  87.358  A08=  49.524  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24=  91.485  A25=  49.524
 Hard: A24=  91.485  A25=  49.524

(Again, remember that we've rotated phi by 90 degrees)


-----

ok, after much counting
combine meshj and meshk and normalize counting time (compare with meshc from January 2011) and we have
two peaks





---------------

11911-->bad from before


-------------------------------------------
Next Film:L021411
3/29/2011,10:30am

      tth    th    chi     phi   
001 35.125 19.901 88.545  0.003
100 35.125 19.942 -3.709 41.403

We go to the 111 in hkk zone

meshl*  two peaks!  Yay!!!!


Finished at 2:25pm
at 111
parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -7.573  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07= 132.262  A08=  42.391  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07= 132.262  A08=  42.391  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24= 135.795  A25=  42.391
 Hard: A24= 135.795  A25=  42.391

---------------------------------------------------------------------------------------------------------

Next Film:L020911(4th film)
3/29/2011,3:30pm

       tth    th     chi      phi   
001  35.125  11.794 87.981   0.004
100  35.125  11.794  1.514  50.173
111  63.020  -0.323 48.503 131.275 ====> in hkk zone

meshm*
15-? tightened area of emphasis
great, two peaks!!!


 dq 1,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
pa
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -0.323  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07= 127.233  A08=  48.503  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07= 127.233  A08=  48.503  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24= 131.275  A25=  48.503
 Hard: A24= 131.275  A25=  48.503



On beam at 3:30pm 3/28/11
Off beam at 12:30 am 3/29/11
----------------------
----------------------
----------------------

Poled +20V

Start with L021411

Find 100 and 001 peaks and then find 111 in hkk zone

       tth    th     chi      phi   
001  35.125  18.908 89.706   0.002
100  35.125  18.908 -2.492  46.475
111  63.020  -5.436 41.834 138.156 ====> in hkk zone

meshn*  (compare to meshl at 0 field)
1-20 .5 .5 .5 two peaks, anything in center?
21-34? .5 .494 .494

% dq 1,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
pa
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -5.463  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07= 134.670  A08=  41.834  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07= 134.670  A08=  41.834  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24= 138.156  A25=  41.834
 Hard: A24= 138.156  A25=  41.834




 

--------------
--------------

L011111  +20V

compare with meshj and meshk combined


recall phi rotated by 90 degrees


hkl  tth th chi phi
001 35.125 11.576 92.299 .001
100 35.125 17.563 1.443 -3.505

see fpx03065 for mosaic
hkk zone

 05:47   1/  1    66.772   63.016
     1.0000  1.0000  1.0000    0.000   *      0:01     2605
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -1.499  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07=  80.786  A08=  49.606  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=  80.786  A08=  49.606  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24=  84.920  A25=  49.606
 Hard: A24=  84.920  A25=  49.606



mesho* decent statistics one peak?

dq 1,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
pa
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.015  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -1.499  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07=  80.786  A08=  49.606  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=  80.786  A08=  49.606  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24=  84.920  A25=  49.606
 Hard: A24=  84.920  A25=  49.606

on beam 5:25am off beam 1:25pm, time on beam 8 hrs



-------------
-------------

Return to L020911 poled -20V (negative)

peak shapes were ugly, so changed slits to 50,50

       tth    th     chi      phi   
001  35.125  10.684 85.035   0.001
100  35.125  10.684 -0.068  50.161

hkk zone

 14:42   1/  1    66.772   63.016
     1.0000  1.0000  1.0000    0.000   *      0:01     2336
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -3.011  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07= 128.071  A08=  51.179  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07= 128.071  A08=  51.179  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  50.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  49.999
 Soft: A24= 132.336  A25=  51.179
 Hard: A24= 132.336  A25=  51.179


compare with meshm
meshp* (half the original counting time...ack!)
ok, statistics weren't enough, so we increased them.  It looks different to my eyes...


RSF: DQ1,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
 RSF: PA
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -3.011  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07= 128.071  A08=  51.179  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07= 128.071  A08=  51.179  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  50.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  49.999
 Soft: A24= 132.336  A25=  51.179
 Hard: A24= 132.336  A25=  51.179



started 3/30  2:30 pm
finished 3/30 7:45 pm
time on beam 5hrs, 15 minutes


 ---------------

 -------------
 -------------


Start with L021411
Poled -20 V (negative)
Find 100 and 001 peaks and then find 111 in hkk zone

       tth    th     chi      phi   
001  35.125  19.595 87.385   0.001
100  35.125  19.595 -4.348  44.633

 20:37   1/  1    66.772   63.016
     1.0000  1.0000  1.0000    0.000   *      0:01     2509
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  -8.968  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07= 136.305  A08=  42.923  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07= 136.305  A08=  42.923  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  50.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  49.999
 Soft: A24= 139.882  A25=  42.923
 Hard: A24= 139.882  A25=  42.923


compare with meshl and meshn
meshq* 2 peaks-->maybe a bit different?

 started 3/30 8:15pm
 stopped 3/31 stopped 2:05am -->6 hrs on beam



 --------------------
 --------------------



L011111  -20V (negative)

compare with 0 voltage=> meshj and meshk combined
compare with mesho==>positive voltage


recall phi rotated by 90 degrees and reset to 0, so current phi values are in that reference system....


hkl  tth th chi phi
001 35.125 14.2357 94.3157 .001
100 35.125 17.563 3.598 -3.354

hkk zone

 03:40   1/  1    66.772   63.016
     1.0000  1.0000  1.0000    0.000   *pa
      0:01     2873
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.016  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=   1.294  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07=  79.209  A08=  46.338  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=  79.209  A08=  46.338  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  50.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  49.999
 Soft: A24=  83.071  A25=  46.338
 Hard: A24=  83.071  A25=  46.338


meshr*

% dq 1,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 1.0000, 1.0000, 1.0000)    A3=  66.772  A4=  63.016
pa
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  66.772  A04=  63.015  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=   1.294  A04=  63.074  A05=  20.831
 Soft: A06=  41.179  A07=  79.209  A08=  46.338  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=  79.209  A08=  46.338  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  50.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  50.000  A15=  49.999
 Soft: A24=  83.071  A25=  46.338
 Hard: A24=  83.071  A25=  46.338



started on beam at 3/31 3:15am
stopped off beam at 3/31 10:00 am
time on beam: 7 hrs

maybe some change...

-----------------
-----------------
-----------------

Let Jeff use the instrument for a day.  Now refreshed we start again, but without a cradle.

This is the L020911 film +20 V (positive)

start with the 110 just for fun
yay, it's there
next, find 100 reflection in the plane.  Then, we'll rotate about it by approximately 45 degrees to find the hkk zone.  Duh!


So, found the 100 at:
a3=12.434, lower tilt (a8=1.418)
next, go to nominal position of 0 0.5 0.5 and try to find scattering plane.


a3 nominal position is 12.319

play with upper tilt
37 to -13

So, found 011 (pretty good job KK!) and optimized it. Then found
100 and optimized.  Fairly close to the UB matrix predicted values, so we should have reproduced the orientation from our last experiment.  Background is pretty good since the sample is mounted on single crystal Si.

Next, check the 111 reflection.  We'll go back and check the slits on the other reflections after this and then set the mesh.

before optimization, tilts at:

 pa7
 Soft: A07=  -4.500
 Hard: A07=  -4.500
% pa8
 Soft: A08=   0.557
 Hard: A08=   0.557

from 100
% pa14
 Soft: A14=  25.000
 Hard: A14=  25.000
% pa15
 Soft: A15=  20.000
 Hard: A15=  19.999
011

optimized tilts again at 011

Check both tilts and a3 at 111 and then run the mesh :>
before:
% pa7
 Soft: A07=  -4.500
 Hard: A07=  -4.500
% pa8
 Soft: A08=  -0.158
 Hard: A08=  -0.158

looks good, set a3 on 111 after optimizing both tilts (pretty close to originals, but need some adjustment)

So, for 111

% pa7
 Soft: A07=  -6.212
 Hard: A07=  -6.212
% pa8
 Soft: A08=  -0.273
 Hard: A08=  -0.273

meshs* compare with meshm and meshp
looks like only one peak...upside down?

Step by step
verified that phi rotation is clockwise.

mesht* -.5 -.5 -.5 one peak.  Physics works.


-----

 Driving to Q = ( 0.0000, 1.0000, 1.0000)    A3=  385.26  A4=  50.518
% pa3
 Soft: A03= 385.259
 Hard: A03= 295.579

-----

-------

Ok, remounted and try again...Bon chance!

started with 0.5 0 0 (lambda/2 of 1 00) reflection with a3=-79.9 calculated

found peak at:
% pa3
 Soft: A03= -81.464
 Hard: A03= -81.464
% pa7
 Soft: A07=   5.822
 Hard: A07=   5.822

in order for this to work with ICP and to agree with UB matrix, we will have to call this -0.5 0 0 (ack!!!!)


did rough alignement on 0 .5 .5
put filters back in and aligned on 0 1 1

 Soft: A03=  25.259
 Hard: A03=  25.314
% pa8
 Soft: A08=   5.162
 Hard: A08=   5.162

after fixing tilt and a3, did slits
a14=a15=30

checked
a% pa3
 Soft: A03= -72.430
 Hard: A03= -72.375
% pa7
 Soft: A07=   5.807
 Hard: A07=   5.807

-1 0 0

checked the width, we'll go with 30 (this one is narrower)

meshu*  2 peaks!!! (killed last scan at meshu078)

% dq 0,1,1
 Parameters used:   3.9091 3.9091 3.9091     011    100
                    90.000 90.000 90.000
 Driving to Q = ( 0.0000, 1.0000, 1.0000)    A3=  25.259  A4=  50.518
% pa
 Soft: A01=  20.589  A02=  41.177  A03=  25.259  A04=  50.518  A05=  20.590
 Hard: A01=  20.707  A02=  41.177  A03=  25.359  A04=  50.518  A05=  20.746
 Soft: A06=  41.179  A07=   5.807  A08=   5.162  A09=   0.000  A10=   0.000
 Hard: A06=  41.393  A07=   5.807  A08=   5.162  A09=   0.000  A10=   0.000
 Soft: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  30.000
 Hard: A11=   0.000  A12=   0.000  A13=   0.000  A14=  30.000  A15=  29.999
 Soft: A24=   6.237  A25=   5.162
 Hard: A24=   6.237  A25=   5.162



The UB matrix is in the last_film_si_mount.txt file
Recall that we are in the plane defined by 0,1,1 and 1,0,0
to get icp to go to the same hardware a3 (yes, we rezeroed it as with the 4 circle), we 
go to -.5 .5 .5 and use -1 0 0 for alignment purposes.


We took photos of 0 1 1 which is along the lower tilt (a8)
Remember which way we're looking--phi is positive clockwise
chi is positive counter clockwise.

collimations were the same as before.

we used realmesh6 and qbuffers 1 and 2 for alignment, qbuffer 20 for scans














 
