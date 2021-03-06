Migrating to Amazon EC2
#######################
:date: 2012-12-02 11:00
:author: Xitij Ritesh Patel
:category: Engineering
:tags: vps, ec2, chromebook

I've been pining over the Google Chromebook lately, as I've been wanting to
become more mobile with my developer setup. In an effort to make this
a reality, I started looking at my options for a VPS.

I currently have two VPSes running, one with prgmr and one with Linode. I've
been very happy with both services, but now I'm becoming concerned with cost.
In total, I spend $28 USD a month. 

If I were to consolidate with Linode, I would have to spend $40/month to get
a VPS with 1GB of RAM. I don't exactly need 1GB of RAM (yet), and it's more
than I currently spend anyway. If I look at prgmr's offerings, I can spend
$20/month and get 1GB of RAM as well. However, the disk space is limited to
24GB. At $36/month, I can get 2GB of RAM and 48GB of disk space. Definitely
more appealing than Linode, if we compare them purely on price.

I started to look at Amazon to see if they could compete on price. The only way
they can is if you reserve a heavy utilization instance, which makes sense
because the instance will be up 100% of the time. If we look at the micro
instance, we can pay $62 for a 1 year term, and get a $0.005/hour instance
rate. If we assume 100% utilization, that works out to $3.66/month. Factor in
our upfront costs, and we end up paying $8.83/month for a micro tier instance
that includes 613MB of RAM. 

However, this doesn't include storage. If we assume
20GB of elastic block storage, this adds $2/month to our bill. At $10.83/month,
I would be paying less than half of what I pay to Linode for an equivalent VPS,
and $1.17 less than what I would pay to prgmr, while getting 101MB more RAM.

This doesn't factor in bandwidth costs, which for my needs is quite minimal.
Looking through my Linode graphs, I generally stay under 5GB total. My highest
usage was November 2011 with 32.54GB total, of which 16.51GB was outbound.
Since Amazon only charges for outbound traffic, we can use this value as the
upperbound, adding another $1.55 to the monthly bill, bringing the total to
$12.38/month. At this price, I would be pay $0.38 more than prgmr, for more RAM
and more disk space, with the extra caveat that I may end up spending more
money on bandwidth should my needs go up. 

For the cost savings, I'm willing to
risk it. If I cared to, I could save even more money by going with a 3 year
term at $100, bringing my monthly amortized costs down to $9.99/month, but I'm
not a huge fan of making such a long-term commitment. 

However, going with EC2 also gives the option of going with a small tier
instance. To keep things fair, I'll increase the elastic block storage size to
48GB. The small tier does come with 160GB of instance storage, but it's not
recommended for use as anything other than temporary storage. With these
features, I would pay $195 up front for the instance, $11.71/month for keeping
it up 100% of the time, $4.80/month for the 48GB EBS volume, and $1.55/month
for the peak bandwidth usage. This amounts to a total monthly amortized cost of
$34.31/month, which is $1.69/month less than prgmr's 2GB RAM option, and
$45.64/month less than Linode's. Moreover, I would only have 1.7GB of RAM with
Amazon's small tier. If I choose to go with the 3 year term, I can reduce this
to $24.20/month due to the reduced hourly rate and increased amortization
period. 

As appealing as the small tier's increased RAM and CPU are, it probably is
overkill for my needs. I need a server to host my blog, websites, VPN, and
e-mail. Since I'm usually the only user, and I've managed with a 512MB Linode
thus far, there doesn't seem to be a need to jump to Amazon's small tier.
Moreover, if I ever need it, I can always spin up another instance. If it
becomes a permanent need, I can resell my micro tier, and reserve a small tier
as needed.

Anyway, we'll see how it works out. 
