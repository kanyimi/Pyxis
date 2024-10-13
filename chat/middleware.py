
# middleware.py
class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)


        # allowed_domains = [
        #     "https://kpyx.co",
        #     "https://www.kpyx.co",
        #     "https://185.100.87.158:8000",
        #     "https://kpyx.io",
        #     "https://www.kpyx.io",
        #     "https://www.krmp.io",
        #     "https://krmp.io",
        #     "https://2krk.site",
        #     "https://portfolio-gzbf.onrender.com",
        #     "https://krm.gg",
        #     "https://knm.st",
        #     "https://2kkm.co",
        #     "https://2kk.site",
        #     "https://2kramp.site",
        #     "https://2kk.ac",
        #     "https://2kkn.ac",
        #     "https://2kkm.st",
        #     "https://torkrn.cc",
        #     "https://torkrn.co",
        #     "https://2krk.in",
        #     "https://2krm.st",
        #     "https://2knmp.cc",
        #     "https://kkn.st",
        #     "https://2kkn.st",
        #     "https://2kkn.top",
        #     "https://tkm.ac",
        #     "https://tkm.cx",
        #     "https://tkm.gg",
        #     "https://2kkm.mx",
        #     "https://2kn.io",
        #     "https://dkm.gg",
        #     "https://2kk.to",
        #     "https://2kk.is",
        #     "https://2kk.ai",
        #     "https://2kk.cx",
        #     "https://2kk.mx",
        #     "https://2kk.sh",
        #     "https://2kk.so",
        #     "https://knmp.cc",
        #     "https://knmp.st",
        #     "https://zerkalo-kra.cc",
        #     "https://zerkalokrn.cc",
        #     "https://dkm.ac",
        #     "https://kr2.ai",
        #     "https://kr2.me",
        #     "https://kr2.is",
        #     "https://km2.is",
        #     "https://4kra.co",
        #     "https://2kn.is",
        #     "https://4kr.co",
        #     "https://t.me",
        #     "https://web.telegram.org",
        #     "https://cyberrpg.gg",
        #     "https://cyberika.gg",
        #     "https://knmp.io",
        #     "https://krn.is",
        #     "https://install.kkrn.co",
        #     "https://cybercity.gg",
        #     "https://km2.ac",
        #     "https://cybertown.gg",
        #     "https://3km.ac",
        #     "https://3km.so",
        #     "https://3km.gg",
        #     "https://kn1.ac",
        #     "http://1kn.ac",
        #     "https://1kn.ac",
        #     "https://kn2.cx",
        #     "https://ddna.top",
        #     "https://kr2.nl",
        #     "https://kuzbass.pro",
        #     "https://mafiacity.gg",
        #     "https://kuzbass.gg",
        #     "https://2kra.tv",
        #     "https://3km.me",
        #     "https://1kn.ac",
        #     "https://1kdm.cc",
        #     "https://1kdm.me",
        #     "https://kn3.me",
        #     "https://3km.nl",
        #     "https://kr-adresa.cc",
        #     "https://mycyber.gg"
        #
        #
        # ]
        allowed_domains = [
            "https://izwup9lqklxynpqndg3d.net",
            "https://4p8ox2caq4cs6tpudhrm.gg",
            "https://rpsu59dbldj3krxr2fs0.org",
            "https://pn3fa5iu35r1chnsie6t.co",
            "https://bjl7xb2umxeshmv8aqft.gg",
            "https://pwmlls2r3j81xr7izglc.info",
            "https://xatar5uo4va2nlt3206o.io",
            "https://kpyx.co",
            "https://ttjrmulobj8fxxw1li7n.io",
            "https://p3ciwy34ajrr9vuq05sf.org",
            "https://6589vb6qoswn0inunuzc.com",
            "https://xhfkobkklplec94ckz4c.com",
            "https://0iz7uw5dpoei945nob6v.org",
            "https://g3vog7jvl6do9v99t11s.info",
            "https://t5k8iz3nbul5ilah05ij.co",
            "https://c58yr9ba43vppx1dyrh7.net",
            "https://www.kpyx.co",
            "https://6589vb6qoswn0inunuzc.com",
            "https://xhfkobkklplec94ckz4c.com",
            "https://185.100.87.158:8000",
            "https://kpyx.io",
            "https://c58yr9ba43vppx1dyrh7.net",
            "https://lk76neaxdjkplxs00jrx.info",
            "https://hlishw36ailsc8vgdl4i.co",
            "https://ueul6sz2n1ci5mupn98e.info",
            "https://jrdfko9a7txpzads0fel.info",
            "https://www.kpyx.io",
            "https://al4b2ye1j6bo40v4k1k2.net",
            "https://dy44b0wd5w50f7cpfdqw.net",
            "https://zylrlioyo8znnxw0jjr1.info",
            "https://m0scbuhxvc384unk4kmm.gg",
            "https://www.krmp.io",
            "https://krmp.io",
            "https://2krk.site",
            "https://f71lu6rjh6mebz1uuo1q.com",
            "https://ustklsssfqoitolu4rc8.co",
            "https://cx1gwsfrlsutly3e6e6b.org",
            "https://ckj8hcs2s2jy89fnlp67.com",
            "https://y04nvgbaan91fcs7y43d.com",
            "https://ee4skxn2376ml4z4milk.io",
            "https://ik6ertr168yxyac8bd81.net",
            "https://portfolio-gzbf.onrender.com",
            "https://krm.gg",
            "https://ejymbev9jdn9p9ay1n9j.info",
            "https://22drb3gz7ixcfupikvz9.co",
            "https://njbpdssqqvl91pu0szz0.ai",
            "https://j5ni8y0a4fvhs5263eml.net",
            "https://knm.st",
            "https://22drb3gz7ixcfupikvz9.co",
            "https://2kkm.co",
            "https://63dwhulrpqeuockf4j65.io",
            "https://crt95quuvd11wl65wn2x.gg",
            "https://myecry82shwhwhob2sva.info",
            "https://ydd2x7i8g030cq6d32lw.co",
            "https://j1jw7qz9auq9j47zrhqi.net",
            "https://2kk.site",
            "https://2kramp.site",
            "https://qln9eae6x2jvbkiioi4i.io",
            "https://pvz13okbd5fmgmimgimd.gg",
            "https://g9qmpbgn4ib2ipof879u.info",
            "https://nbmq7seq3xbotkd4b9ii.org",
            "https://2kk.ac",
            "https://2kkn.ac",
            "https://2kkm.st",
            "https://torkrn.cc",
            "https://mgco8g3hp6nl1ekg2ycr.co",
            "https://7azkqtoc33ykuhbkzi8j.info",
            "https://s906j735g8k4esqdzu7c.org",
            "https://z95lb2kp9i4putg7sjvf.gg",
            "https://zo9doue6yqnsmnhmzth1.info",
            "https://torkrn.co",
            "https://2krk.in",
            "https://2krm.st",
            "https://njj6577d0ofgrpn4g3dl.co",
            "https://2w2hujq07lsqnvg178pf.io",
            "https://d31tu6562dv7xbg16txv.co",
            "https://55yelz28fy9e4ji1aoe2.io",
            "https://n3w6omd5jblsbaswmq84.com",
            "https://fvfmtbymw49be0e9lvc6.gg",
            "https://p3nj727b68eope0og9b0.com",
            "https://2knmp.cc",
            "https://kkn.st",
            "https://2kkn.st",
            "https://7tbdg38d8oje3i2juvg9.ai",
            "https://cttjz8ugy8surlo40ey5.ai",
            "https://khnf1chxem13nvc6iywn.gg",
            "https://cb4pfq9g0rkbrp3ochzo.net",
            "https://bf1gv0uta2rck1hqy151.co",
            "https://exbacair2ouvyx9pl2pw.net",
            "https://8s3htitxh9qosz4f53zf.gg",
            "https://wt6ewsouz71agetkhm3e.net",
            "https://2kkn.top",
            "https://tkm.ac",
            "https://4qtingu6wx8qpbjdh1oj.info",
            "https://wkeoa7mp48qzjloy01d1.info",
            "https://6j8yz6e1s825pfo42bf2.org",
            "https://1tkk4t0ijqxhtffkx9lx.org",
            "https://v8q1ou6qdpfd3902v6sf.gg",
            "https://2krm.in",
            "https://ysn7ogamqj34iotqwyr8.net",
            "https://2i0pfyp2hh40bolj2pcq.ai",
            "https://622dh0bgs0x79fey86qj.co",
            "https://tkm.cx",
            "https://tkm.gg",
            "https://zh125x6u2hc0rbhqw0dz.info",
            "https://dwasxrl00a08txjtluuh.info",
            "https://fif5lqc69qwtsvf08o68.net",
            "https://asc9gveu5t4f0483b53l.io",
            "https://2g9p4zoxyrrn12s4mxq2.co",
            "https://1m71q8k1cmxmjcbg4lc6.gg",
            "https://yr2z91jp8enrf36c5wix.info",
            "https://2kkm.mx",
            "https://2kn.io",
            "https://48jmbrr8i8xm1t4xmqlw.io",
            "https://88rmbcif7iootvjr8q2g.info",
            "https://bn21gjigc3hkenlmxdl0.gg",
            "https://txsc02x9cd67r35ifdyo.io",
            "https://1845mxmai2zfjrn38xvm.org",
            "https://3x2kg42s4zgc1swwohkd.org",
            "https://dkm.gg",
            "https://2kk.to",
            "https://0rssfz6kfmxocjxgtqxk.com",
            "https://gbf9uadugf7beorioi32.net",
            "https://bd8169kdpjwzhbalz7iu.net",
            "https://n5sl9pt71q1bmicaib93.ai",
            "https://dnmrfkx7nm9uv0di4rx0.io",
            "https://h0v4s9sedeldb66d38uq.info",
            "https://2kk.is",
            "https://2kk.ai",
            "https://e137lr44f6a0dxohyklx.ai",
            "https://98ch4khqac3ew0905l5b.ai",
            "https://vr0n9sy7vr4p2ltjdhcv.com",
            "https://9a9q7r89ovtsjkgdrghf.com",
            "https://cdalyebxl7mennw07rvr.org",
            "https://5knjuzskuudnx6fndvx5.gg",
            "https://3jornhm3i2vkgg9c4f37.net",
            "https://2kk.cx",
            "https://2kk.mx",
            "https://j0onaem0q8m62jac4oco.info",
            "https://o0dvk38c3liacljudnf5.info",
            "https://w8011jmi8e45ijr1m1j9.co",
            "https://8jzuzthptzgcd0sr4auf.io",
            "https://mmhmhle483lx5b1h2zyp.io",
            "https://m2c3jqaszivr6wty27yx.org",
            "https://2kk.sh",
            "https://85kzopwzfnwhdyqfowpa.info",
            "https://0ko9g6jhvf6hm85tw6cg.org",
            "https://a1h4ga8rwvl7y9h8izg5.info",
            "https://vs56s8v42yh2apcheldl.net",
            "https://0e7r30sswqre02hg4bm8.info",
            "https://az81j7hdmj6g8co17t8z.io",
            "https://lo4j180dwpaa7sfi5w8q.gg",
            "https://ag3qk49d56i4cj1ez9b9.ai",
            "https://p4kopin6yaualcwfbnp9.ai",
            "https://2kk.so",
            "https://knmp.cc",
            "https://knmp.st",
            "https://zerkalo-kra.cc",
            "https://dcleb5k8299xpwyi4xoy.io",
            "https://yfqj76lzjiod1qhaad1q.org",
            "https://sdulzb55lewdrv55nhaa.co",
            "https://zndhna8mzrkom42xrl7l.info",
            "https://5u256ih28wim6r202lnx.io",
            "https://ak9zf43dbyrupz1a30bz.info",
            "https://xyf43ud8bmcln6rhouwh.org",
            "https://bwznu4p5bxbo1461a4l6.net",
            "https://7tydemtcsa8jxhylwyex.info",
            "https://zerkalokrn.cc",
            "https://dkm.ac",
            "https://kr2.ai",
            "https://7tydemtcsa8jxhylwyex.info",
            "https://6hm5ye9b53kxn4acvhbn.info",
            "https://dsin21bneii2lopj69vk.io",
            "https://55zdzmsk30ysngii008o.co",
            "https://xtakw8y63ipgtlwban9z.com",
            "https://zfzrqs6x5xcjk2s17ove.ai",
            "https://1xfz3vezk0ufg33vlwvo.co",
            "https://m0t3n0utwfgo3llnpkk6.net",
            "https://c00bextujbunnv750i4t.net",
            "https://sl2nf25xerzoz1g9myve.ai",
            "https://or1o3givwvnb0hbr9mkh.info",
            "https://kr2.me",
            "https://kr2.is",
            "https://443aigb5mkibd7trtgpt.io",
            "https://e047og0dsu0p4xu471jw.org",
            "https://g7y6aq6as8c7zolot8af.co",
            "https://1vzafkeso0tkwlfnb1av.info",
            "https://v51tv3kpv1i7hq7a7qo6.co",
            "https://msz85zwbkf3ks101gmdb.org",
            "https://wjxuxn16kkit4tix5zga.com",
            "https://lsmu2t4apar84om4lq6k.org",
            "https://evy27r5avba1nmw8ivvo.gg",
            "https://km2.is",
            "https://4kra.co",
            "https://0t2jodpohs287xo7gcbi.co",
            "https://1844cfzrdcvp4xd9vidh.gg",
            "https://6sflp4v7noavhn76lqr2.io",
            "https://bs6cb7lqkd518if4dwty.io",
            "https://k010gxnro40m4aocuhid.org",
            "https://bnfnsphemx4u7h6evspt.gg",
            "https://9rficaafh9xsusbceoy1.info",
            "https://lo3ot1ib7s3r671b3dk5.org",
            "https://2kn.is",
            "https://4kr.co",
            "https://tlbs5mc206rbkl7x62s9.gg",
            "https://8oq5t5hqjtfncpsef3uj.info",
            "https://n523dha214lpy9wkigq1.io",
            "https://392vn42gf4sf9bwix5o5.co",
            "https://anczcvof805h9u30an3y.gg",
            "https://wbv2asxgx3zbj0ffygri.info",
            "https://3l5si7n9vm87zw1wjzqb.ai",
            "https://oz35x9vi81csvxnrrqxf.com",
            "https://81ooh5984votira33e1x.io",
            "https://0dacvirohvpmc5tfyt5c.org",
            "https://ebohpyr4dv9bh9wlggai.info",
            "https://x1m5plw8sycurgdp5f4m.gg",
            "https://t.me",
            "https://web.telegram.org",
            "https://cyberrpg.gg",
            "https://0ot49czukm5z5ruxri1s.ai",
            "https://9syvfy1g32ieengkyc8m.com",
            "https://rppsff1s8fxlyzt4buqn.org",
            "https://j9d23veh2yi7p1e1isao.org",
            "https://44z28tdmgu78qn1f7eh5.com",
            "https://pbn31wqejzgwl05yfe77.info",
            "https://a77jfjxrfvvf4y3ia3o1.gg",
            "https://ci8p58nnfq9zeyg7yjjz.info",
            "https://qfcpxf4u2sltvp37jryh.co",
            "https://uao0ifh70vjiiekriobg.com",
            "https://ncc62jpp1zgpim8icq8j.io",
            "https://s1qaup05no877xo5oeyr.ai",
            "https://41o57g09gxx67dp4382w.org",
            "https://cyberika.gg",
            "https://knmp.io",
            "https://krn.is",
            "https://install.kkrn.co",
            "https://7chpv7isbgl0j5n9r0vh.com",
            "https://ltqo5hmbqf309dq9bwi2.info",
            "https://rmeslj4075zqvi4zc6mj.ai",
            "https://kotkjjc9mqceis5mr0gj.co",
            "https://lla6j41hajg2ngrg191c.org",
            "https://umze3kynb5gojm3z636c.org",
            "https://cybercity.gg",
            "https://km2.ac",
            "https://cybertown.gg",
            "https://3km.ac",
            "https://3km.so",
            "https://3km.gg",
            "https://m27crag4rtdsfrkp3y1p.ai",
            "https://5yiz3z2g8o3yvdq4373j.info",
            "https://nf8nfnzhd5fha25sh14g.co",
            "https://rszara2zll18pj8grkin.gg",
            "https://kn1.ac",
            "http://1kn.ac",
            "https://4aknz28ji7l6l5wgug4p.org",
            "https://qm9lmtf9nmgfeik49e9h.co",
            "https://5m6fn8ssv8s0l9dllhsy.net",
            "https://1oit8g58l473xeqfk0p1.gg",
            "https://7jgokbi7ezv409jialb6.co",
            "https://1kn.ac",
            "https://kn2.cx",
            "https://v3pqo4nrtq3s3xji9szv.co",
            "https://bp52z7c3mi6az0prj66s.com",
            "https://58gzxtt6ul472ss4tq3g.com",
            "https://579377dvddx82uszc5bi.org",
            "https://ddna.top",
            "https://gf2z4dlecapmukjtul6y.io",
            "https://kevf68aa6k4auqghukto.org",
            "https://y4durg9harij3j83wbqq.co",
            "https://5wbkciom3hsm84s37ag0.org",
            "https://ewantl4wgqwjk157kz01.org",
            "https://kr2.nl",
            "https://kd0tiu0ej3zvv15ezek6.co",
            "https://f8txxmjwhwipehsse9ia.gg",
            "https://ukufcn3xzwubyuq2ma42.info",
            "https://stv9wc4f21kvblggnk99.co",
            "https://pnhfob5j4gm1kv00ko1n.gg",
            "https://kuzbass.pro",
            "https://mafiacity.gg",
            "https://em5ib4u1ivix9ybmnc5b.org",
            "https://sfinw8x9abbswi1iazjr.io",
            "https://a3vmq03pek0ts0a4dgmm.net",
            "https://21m4kd1grn5kx7jcqt3h.com",
            "https://a3shsnrmgbcyul0v1ckh.org",
            "https://gw50cqn8b02vg3dbkkqw.ai",
            "https://19efnj0ry0dz078dl8bm.net",
            "https://vzgah4bz904tlitmqqzw.co",
            "https://c23eu809yma1yq0y5bkq.ai",
            "https://kuzbass.gg",
            "https://2kra.tv",
            "https://3km.me",
            "https://1kn.ac",
            "https://1kdm.cc",
            "https://1kdm.me",
            "https://kn3.me",
            "https://3km.nl",
            "https://kr-adresa.cc"

        ]

        frame_ancestors = ' '.join(allowed_domains)


        response['Content-Security-Policy'] = f"frame-ancestors {frame_ancestors}"

        return response
