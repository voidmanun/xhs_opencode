### 获取评论列表
调用方式
```
sh fetchMentions.sh
```

评论列表返回格式如下,核心字段comment_info.content,表示用户真实评论,item_info.id,表示笔记id
```
{
    "success": true,
    "msg": "成功",
    "data": {
        "strCursor": "7605572378756413458",
        "message_list": [
            {
                "id": "7611765090237675191",
                "time": 1772252165,
                "score": 7611765090237675191,
                "comment_info": {
                    "content": "这是哪里啊",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0,
                    "target_comment": {
                        "status": 0,
                        "liked": false,
                        "like_count": 0,
                        "id": "69a0130f00000000190006dd",
                        "content": "刚去[图片]",
                        "illegal_info": {
                            "status": 0,
                            "desc": "",
                            "illegal_status": "NORMAL"
                        },
                        "user_info": {
                            "nickname": "低配玩家小马",
                            "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                            "red_official_verify_type": 0,
                            "userid": "5b11e34711be10479b461863"
                        },
                        "image_list": [
                            "http://sns-img-qc.xhscdn.com/comment/1040g4b831t20i9molm004a5rrihke633r8f3io8"
                        ]
                    },
                    "id": "69a26c010000000008030fd2"
                },
                "time_flag": 0,
                "type": "comment/comment",
                "title": "回复了你的评论",
                "user_info": {
                    "userid": "59e040d16eea88393e2b709a",
                    "nickname": "露露露露露",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/59e040d5d1d3b960f40f4865.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "AB8f-9ENe5YMjskF5MkyY2GtxbdHr50eRSJaXx9O8Afp0="
                },
                "item_info": {
                    "type": "note_info",
                    "image": "http://ci.xiaohongshu.com/notes_pre_post/1040g3k031t1uuqln5c005om6go40voaoq054g60?imageView2/2/w/1080/format/jpg",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/notes_pre_post/1040g3k031t1uuqln5c005om6go40voaoq054g60?imageView2/2/w/1080/format/jpg",
                        "width": 1920,
                        "height": 2560
                    },
                    "link": "xhsdiscover://item/discovery.69a0087a0000000022022fcb?type=normal&sourceID=notifications&feedType=single&anchorCommentId=69a26c010000000008030fd2&authorId=62c68608000000000303e158",
                    "status": 0,
                    "id": "69a0087a0000000022022fcb",
                    "content": "杭州元宵活动汇总🏮赶紧查收～看元宵灯会",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "user_info": {
                        "nickname": "ThreeLadies 生活实录",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31re5p8ut70005om6go40voao184kp68?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0,
                        "userid": "62c68608000000000303e158"
                    },
                    "xsec_token": "LBzQRfIfgVBcrDcrc089EuvOgAcgsJ_3gg0yBhE5SwNP8="
                },
                "track_type": "26",
                "liked": false
            },
            {
                "id": "7611346966580629251",
                "type": "comment/comment",
                "title": "回复了你的评论",
                "score": 7611346966580629251,
                "item_info": {
                    "type": "note_info",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "xsec_token": "LB-1wCwjd-goZ8UOfZg4U-QvXG36wGED7zBKYDlkO5ZN8=",
                    "id": "670d10120000000021005d8c",
                    "content": "黑神话悟空高周目大圣怎么打？一套公式通解",
                    "image_info": {
                        "height": 1656,
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                        "width": 1242
                    },
                    "link": "xhsdiscover://item/discovery.670d10120000000021005d8c?type=video&sourceID=notifications&feedType=single&anchorCommentId=69a0efba0000000006032a37&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马"
                    },
                    "status": 0
                },
                "track_type": "40",
                "time_flag": 0,
                "time": 1772154813,
                "user_info": {
                    "userid": "5d38100f0000000012021266",
                    "nickname": "娜姐",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/7121a416be8e543266fd62c1cc9d575e.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "indicator": "你的粉丝",
                    "xsec_token": "ABLmSH_Xvt5IEqgOORlWmuoX7_yj5v1XPzI_2hS7oYfvc="
                },
                "comment_info": {
                    "status": 0,
                    "liked": true,
                    "like_count": 1,
                    "target_comment": {
                        "illegal_info": {
                            "status": 0,
                            "desc": "",
                            "illegal_status": "NORMAL"
                        },
                        "user_info": {
                            "nickname": "低配玩家小马",
                            "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                            "red_official_verify_type": 0,
                            "userid": "5b11e34711be10479b461863"
                        },
                        "status": 0,
                        "liked": false,
                        "like_count": 1,
                        "id": "69a063a3000000000900727b",
                        "content": "装备带对就可以了啊"
                    },
                    "id": "69a0efba0000000006032a37",
                    "content": "谢谢主播用你的方法终于过了",
                    "illegal_info": {
                        "illegal_status": "NORMAL",
                        "status": 0,
                        "desc": ""
                    }
                },
                "liked": false
            },
            {
                "time_flag": 0,
                "id": "7611177581660418693",
                "type": "comment/item",
                "title": "评论了你的笔记",
                "time": 1772115375,
                "item_info": {
                    "status": 0,
                    "xsec_token": "LB-1wCwjd-goZ8UOfZg4U-QvXG36wGED7zBKYDlkO5ZN8=",
                    "type": "note_info",
                    "content": "黑神话悟空高周目大圣怎么打？一套公式通解",
                    "link": "xhsdiscover://item/discovery.670d10120000000021005d8c?type=video&sourceID=notifications&feedType=single&anchorCommentId=69a055ac000000000600e761&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马"
                    },
                    "id": "670d10120000000021005d8c",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    }
                },
                "comment_info": {
                    "id": "69a055ac000000000600e761",
                    "content": "主播为什么你的伤害那么高",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0
                },
                "score": 7611177581660418693,
                "user_info": {
                    "red_official_verify_type": 0,
                    "indicator": "你的粉丝",
                    "xsec_token": "ABLmSH_Xvt5IEqgOORlWmuoX7_yj5v1XPzI_2hS7oYfvc=",
                    "userid": "5d38100f0000000012021266",
                    "nickname": "娜姐",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/7121a416be8e543266fd62c1cc9d575e.jpg?imageView2/2/w/120/format/jpg"
                },
                "track_type": "41",
                "liked": false
            },
            {
                "item_info": {
                    "content": "黑悟空获取最强技能禁子诀，翠笠武师速杀",
                    "image_info": {
                        "width": 1242,
                        "height": 1656,
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k03174kebp70o004a5rrihke633r2t3kl8?imageView2/2/w/1080/format/jpg"
                    },
                    "link": "xhsdiscover://item/discovery.66d1dce0000000001d03b5b8?type=video&sourceID=notifications&feedType=single&anchorCommentId=699d1756000000001803b63f&authorId=5b11e34711be10479b461863",
                    "status": 0,
                    "type": "note_info",
                    "id": "66d1dce0000000001d03b5b8",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k03174kebp70o004a5rrihke633r2t3kl8?imageView2/2/w/1080/format/jpg",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "user_info": {
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马"
                    },
                    "xsec_token": "LBWJ_-8Q8gk47WE1OgTs-q97LVLEYxsQgfXQCJs_s8K9o="
                },
                "comment_info": {
                    "id": "699d1756000000001803b63f",
                    "content": "还可以",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0
                },
                "track_type": "41",
                "liked": false,
                "type": "comment/item",
                "title": "评论了你的笔记",
                "time": 1771902809,
                "score": 7610264617641761386,
                "user_info": {
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31n65bj0r5m005p3ltsu9eh63937rc98?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABeo-Zqtop5G4ygB7_NiPjhigZqdvJ-967Xt3gVG13Y-Q=",
                    "userid": "6475ef3c00000000250344c3",
                    "nickname": "法学司机"
                },
                "time_flag": 0,
                "id": "7610264617641761386"
            },
            {
                "user_info": {
                    "nickname": "小红薯68188064",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/645b6abf2e368555521befcc.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABsBvMNLkn3roppuSZ6jR86KFZKuLcsliuT5FzsU3WHJw=",
                    "userid": "681731b1000000000e01114d"
                },
                "id": "7610081239719519638",
                "type": "comment/item",
                "score": 7610081239719519638,
                "item_info": {
                    "type": "note_info",
                    "content": "黑神话悟空白衣秀士怎么打？一棒打死",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g34o3177rmigjgs0g4a5rrihke633lna48ig?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "xsec_token": "LB_k0EwC818wqnwEcHlN99sIvk-eQC5u704XeWkfhhFeI=",
                    "id": "66d51136000000001d0156d6",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g34o3177rmigjgs0g4a5rrihke633lna48ig?imageView2/2/w/1080/format/jpg",
                    "link": "xhsdiscover://item/discovery.66d51136000000001d0156d6?type=video&sourceID=notifications&feedType=single&anchorCommentId=699c708e00000000040015dc&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg"
                    }
                },
                "comment_info": {
                    "id": "699c708e00000000040015dc",
                    "content": "我46级还过不到[哭惹R]。不想玩了。",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0
                },
                "track_type": "41",
                "liked": false,
                "time_flag": 0,
                "title": "评论了你的笔记",
                "time": 1771860113
            },
            {
                "comment_info": {
                    "liked": true,
                    "like_count": 1,
                    "id": "6999a92300000000060094b1",
                    "content": "太牛了吧，重复打了十几次看了好多攻略过不了，这个视频看两遍一次就过了，我的妈呀博主我一人血书推你上感动中国！！！！",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0
                },
                "track_type": "41",
                "liked": false,
                "time_flag": 0,
                "score": 7609299035979016849,
                "type": "comment/item",
                "title": "评论了你的笔记",
                "time": 1771677992,
                "user_info": {
                    "red_official_verify_type": 0,
                    "xsec_token": "ABJF-0VGI4i0HKB2dQrTMXVedpSjGC5FWSpl3ElOOPQsg=",
                    "userid": "5cf934d90000000025006180",
                    "nickname": "momo",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31ci9dvkdh2005n7p6jcp8oc0srnoqlo?imageView2/2/w/120/format/jpg"
                },
                "item_info": {
                    "id": "66cc829a000000001d01ac58",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "link": "xhsdiscover://item/discovery.66cc829a000000001d01ac58?type=video&sourceID=notifications&feedType=single&anchorCommentId=6999a92300000000060094b1&authorId=5b11e34711be10479b461863",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g34o316vd5l2b0q0g4a5rrihke6335dqecr0?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "status": 0,
                    "xsec_token": "LB7mvJ4GtGWkfRSl7u5aX6mrWkCVZUnnAV2O2S4BtfDNM=",
                    "type": "note_info",
                    "content": "黑神话悟空最简单打法，隐藏BOSS小骊龙逃课",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g34o316vd5l2b0q0g4a5rrihke6335dqecr0?imageView2/2/w/1080/format/jpg"
                },
                "id": "7609299035979016849"
            },
            {
                "title": "评论了你的笔记",
                "user_info": {
                    "userid": "635a0d87000000001901e06a",
                    "nickname": "迷途之羊",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/6562214b2afdbd5a4a7dc784.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABHhR3n3OFc41XfKJ_Nrxmbs3K3N8AFXbWA3gkgWwApOw="
                },
                "track_type": "41",
                "time_flag": 0,
                "id": "7609282891198264785",
                "time": 1771674233,
                "score": 7609282891198264785,
                "item_info": {
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k031bebfisp7i004a5rrihke633kcp74to?imageView2/2/w/1080/format/jpg",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "xsec_token": "LB6jh6lLrGXwy00-lDDhX0EebDEdOrkcnCxc33eDfjmUw=",
                    "user_info": {
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马"
                    },
                    "status": 0,
                    "type": "note_info",
                    "id": "675ee34b0000000007008ca5",
                    "content": "黑神话悟空万样骁凶攻略，超低门槛逃课打法",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k031bebfisp7i004a5rrihke633kcp74to?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "link": "xhsdiscover://item/discovery.675ee34b0000000007008ca5?type=video&sourceID=notifications&feedType=single&anchorCommentId=69999a750000000004002450&authorId=5b11e34711be10479b461863"
                },
                "comment_info": {
                    "status": 0,
                    "liked": true,
                    "like_count": 1,
                    "id": "69999a750000000004002450",
                    "content": "牛逼，已过",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    }
                },
                "liked": false,
                "type": "comment/item"
            },
            {
                "track_type": "41",
                "liked": false,
                "time_flag": 0,
                "id": "7609222748769767423",
                "title": "评论了你的笔记",
                "user_info": {
                    "xsec_token": "ABvZ4fhkFYxMmZ2jarx05km8fByvAavt9UnIGXbcj3AyQ=",
                    "userid": "5b572d4ce8ac2b525cab48e3",
                    "nickname": "momo",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31dc26vatgm004a7fhmmkoi73nd1a6a8?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0
                },
                "item_info": {
                    "content": "明末:张献忠，这BOSS就是为了这把刀设计的",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k031kuqleh7ia004a5rrihke6334b3coug?imageView2/2/w/1080/format/jpg",
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "status": 0,
                    "xsec_token": "LBHBCYl96SoLG6ntc7F0uMCk7jMKMGP6_FzCAZ3oV8P80=",
                    "type": "note_info",
                    "id": "6896abec0000000023037127",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k031kuqleh7ia004a5rrihke6334b3coug?imageView2/2/w/1080/format/jpg",
                        "width": 1263,
                        "height": 1685
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "link": "xhsdiscover://item/discovery.6896abec0000000023037127?type=video&sourceID=notifications&feedType=single&anchorCommentId=699963c1000000000c00a450&authorId=5b11e34711be10479b461863"
                },
                "comment_info": {
                    "id": "699963c1000000000c00a450",
                    "content": "什么玩意 为什么我是刮痧[叹气R]",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0
                },
                "type": "comment/item",
                "time": 1771660230,
                "score": 7609222748769767423
            },
            {
                "item_info": {
                    "type": "note_info",
                    "id": "693d6fe5000000001e0381d1",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g34o31q1ltmeq6u104a5rrihke6335fjnulo?imageView2/2/w/1080/format/jpg",
                        "width": 1011,
                        "height": 1348
                    },
                    "status": 0,
                    "xsec_token": "LBcyUEsrGD1xfPs4CsvtMkJE8PnnLoyKvIiGoPVGvXX9A=",
                    "content": "33号远征队能这么成功，他们才是最大的功臣",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g34o31q1ltmeq6u104a5rrihke6335fjnulo?imageView2/2/w/1080/format/jpg",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "link": "xhsdiscover://item/discovery.693d6fe5000000001e0381d1?type=video&sourceID=notifications&feedType=single&anchorCommentId=699836dd0000000003012db6&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    }
                },
                "liked": false,
                "title": "评论了你的笔记",
                "score": 7608891911734802454,
                "user_info": {
                    "nickname": "风筝cf",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31svdqoj35m6g5q1dpfsjlikoh2rm8d8?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABkro8h01441fsSl3vNL_XpFDrBwgVPKmJY0DE-Zb6CVM=",
                    "userid": "682dcbf9000000000e02ca98"
                },
                "comment_info": {
                    "target_comment": {
                        "illegal_info": {
                            "status": 0,
                            "desc": "",
                            "illegal_status": "NORMAL"
                        },
                        "user_info": {
                            "userid": "5e02306b000000000100bef2",
                            "nickname": "慕",
                            "image": "https://sns-avatar-qc.xhscdn.com/avatar/c94b2589011be6d87bfbbbf21db9e2a0.jpg?imageView2/2/w/120/format/jpg",
                            "red_official_verify_type": 0
                        },
                        "status": 0,
                        "liked": false,
                        "like_count": 42,
                        "id": "693fb33f000000001d01fd14",
                        "content": "慕: 我不觉得高开低走，这其实是人类有史以来一直没有一个确切答案的恒古命题，就是电车难题。到底是一条轨道上家人被绑着重要，还是另一条轨道上被绑着的一个世界的人重要，这其实才是引人深思的问题。我反而认为他宏大到震慑人心。不论如何，我最后选择了用一生去绘"
                    },
                    "id": "699836dd0000000003012db6",
                    "content": "我觉得不是电车难题，而是谈论虚拟和现实的选择，传统价值观是批判一切逃避现实的行为的，但是这个游戏把虚拟放在跟现实同等地位，最后让玩家自己选择，它提出的议题是：如果现实的残酷就像降维打击，且难以改变，那为何我们还必须去面对？比如有人一出生就是残疾人，他需要付出比健全人更多的努力才能把生活过好，但这对他公平吗？命运本就对他如此不公，为何还不能选择逃避进虚拟的世界里来获得一丝安慰？比如他可以沉浸在小说、游戏等虚拟世界里，至少在虚拟世界里他可以当个健全人。这个命题并不局限于家庭或个人，它还可以放大到整个国家，家庭只是个缩影罢了。",
                    "illegal_info": {
                        "desc": "原评论已删除",
                        "illegal_status": "DELETE",
                        "status": 1
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0
                },
                "track_type": "42",
                "time_flag": 0,
                "id": "7608891911734802454",
                "type": "comment/comment",
                "time": 1771583201
            },
            {
                "liked": false,
                "id": "7608818828570526739",
                "type": "comment/item",
                "score": 7608818828570526739,
                "user_info": {
                    "userid": "592ba3e56a6a690b176030e0",
                    "nickname": "小红薯1548625",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/621facc90aa366f8d2f66ba2.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABi1uDZuJ579s7-WSdalIsmUsPzkSJRUQmu4g1RifVoc8="
                },
                "item_info": {
                    "type": "note_info",
                    "id": "66caa65c000000001d03b297",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k0316tiu9740m004a5rrihke6332057bjg?imageView2/2/w/1080/format/jpg",
                    "link": "xhsdiscover://item/discovery.66caa65c000000001d03b297?type=video&sourceID=notifications&feedType=single&anchorCommentId=6997f4650000000006031ba6&authorId=5b11e34711be10479b461863",
                    "status": 0,
                    "content": "黑神话悟空无赖逃课打法，石先锋一招搞定",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k0316tiu9740m004a5rrihke6332057bjg?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "xsec_token": "LBDqcqsYsDxWE2XFGwTapfXgBSJ1i-HlxgS05kacIHsEA="
                },
                "title": "评论了你的笔记",
                "time": 1771566185,
                "comment_info": {
                    "like_count": 0,
                    "id": "6997f4650000000006031ba6",
                    "content": "为什么我蓄棍后总是打不中它",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": false
                },
                "track_type": "41",
                "time_flag": 0
            },
            {
                "track_type": "41",
                "liked": false,
                "id": "7608465026345886051",
                "type": "comment/item",
                "title": "评论了你的笔记",
                "time": 1771483809,
                "comment_info": {
                    "liked": false,
                    "like_count": 0,
                    "id": "6996b29d000000000f02a20d",
                    "content": "我 44 级了还用看你这个教学？？？",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0
                },
                "score": 7608465026345886051,
                "user_info": {
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/60f1dc910c6c5b99c676ca13.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABocUDeA5p5J53PyE0DD2lGVS1F4bdd-HCNGYQKMCRUso=",
                    "userid": "60f1dc66000000000101faae",
                    "nickname": "磊哥"
                },
                "item_info": {
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g34o316vd5l2b0q0g4a5rrihke6335dqecr0?imageView2/2/w/1080/format/jpg",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g34o316vd5l2b0q0g4a5rrihke6335dqecr0?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "link": "xhsdiscover://item/discovery.66cc829a000000001d01ac58?type=video&sourceID=notifications&feedType=single&anchorCommentId=6996b29d000000000f02a20d&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "xsec_token": "LB7mvJ4GtGWkfRSl7u5aX6mrWkCVZUnnAV2O2S4BtfDNM=",
                    "content": "黑神话悟空最简单打法，隐藏BOSS小骊龙逃课",
                    "id": "66cc829a000000001d01ac58",
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "status": 0,
                    "type": "note_info"
                },
                "time_flag": 0
            },
            {
                "id": "7608000478386791624",
                "type": "comment/comment",
                "title": "评论了你的笔记",
                "time": 1771375648,
                "score": 7608000478386791624,
                "comment_info": {
                    "like_count": 0,
                    "target_comment": {
                        "status": 0,
                        "liked": false,
                        "like_count": 15,
                        "id": "67cd60bb0000000018005321",
                        "content": "Tao:): 手柄不是更难点嘛…",
                        "illegal_info": {
                            "status": 1,
                            "desc": "原评论已删除",
                            "illegal_status": "DELETE"
                        },
                        "user_info": {
                            "userid": "62fa6bfc000000001200d8c7",
                            "nickname": "Tao:)",
                            "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo315d6qt49ha005onqdfu4hm67bkgl7f8?imageView2/2/w/120/format/jpg",
                            "red_official_verify_type": 0
                        }
                    },
                    "id": "69950c1d000000000800ee9b",
                    "content": "手柄不是更简单吗？我就是用的手柄",
                    "illegal_info": {
                        "status": 1,
                        "desc": "原评论已删除",
                        "illegal_status": "DELETE"
                    },
                    "status": 0,
                    "liked": false
                },
                "user_info": {
                    "userid": "614027f80000000002025fa3",
                    "nickname": "再临",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31sajiok8m80g5oa04vs0knt3rhbue40?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABDa180dXsjBPtVEt-XofEc8YLFZtcx96wMAn5toEq4ME="
                },
                "item_info": {
                    "content": "和老婆双影奇境，刚打完了教学关，已破防",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k031f1sohmjmq004a5rrihke63357bhtr8?imageView2/2/w/1080/format/jpg",
                    "link": "xhsdiscover://item/discovery.67cd20370000000029032c01?type=video&sourceID=notifications&feedType=single&anchorCommentId=69950c1d000000000800ee9b&authorId=5b11e34711be10479b461863",
                    "id": "67cd20370000000029032c01",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k031f1sohmjmq004a5rrihke63357bhtr8?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "user_info": {
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg"
                    },
                    "status": 0,
                    "xsec_token": "LBnO5pAYXARELMagDT1yIHDac-JOCy7sO0D4t_6E63jN0=",
                    "type": "note_info"
                },
                "track_type": "42",
                "liked": false,
                "time_flag": 0
            },
            {
                "liked": false,
                "time_flag": 0,
                "title": "评论了你的笔记",
                "time": 1771045808,
                "user_info": {
                    "nickname": "weipeixiaoxiao",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/5f80626cb6a9920001c3d737.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABydqENadmg-oC_zcJLhGC3JouOvTGUFN3h0WvHKpxEEk=",
                    "userid": "552dc4a12e1d930ef8866d43"
                },
                "item_info": {
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "status": 0,
                    "xsec_token": "LB-1wCwjd-goZ8UOfZg4U-QvXG36wGED7zBKYDlkO5ZN8=",
                    "type": "note_info",
                    "id": "670d10120000000021005d8c",
                    "content": "黑神话悟空高周目大圣怎么打？一套公式通解",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "link": "xhsdiscover://item/discovery.670d10120000000021005d8c?type=video&sourceID=notifications&feedType=single&anchorCommentId=699003ad00000000050317ca&authorId=5b11e34711be10479b461863"
                },
                "track_type": "41",
                "id": "7606583826374149006",
                "type": "comment/item",
                "score": 7606583826374149006,
                "comment_info": {
                    "like_count": 1,
                    "id": "699003ad00000000050317ca",
                    "content": "这套公式是很好用，但是芭蕉扇快结束的时候，无量佛到最后总是冻不住，最后我磕药把它磕过去了",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": true
                }
            },
            {
                "user_info": {
                    "red_official_verify_type": 0,
                    "xsec_token": "AB28N-VWRPhcyjcVOGx0vGTtdhdqd0ZUOVloKaC5EV97Q=",
                    "userid": "6602c0f7000000000b03186e",
                    "nickname": "鱼缸缸缸",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31t4kdmts5s005pg2o3riu63ekd4b7jo?imageView2/2/w/120/format/jpg"
                },
                "comment_info": {
                    "id": "698fc83b000000000800e199",
                    "content": "@苹果鱼🍏🐟",
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "status": 0,
                    "liked": true,
                    "like_count": 1
                },
                "track_type": "41",
                "time": 1771030588,
                "type": "comment/item",
                "title": "评论了你的笔记",
                "score": 7606518456971543308,
                "item_info": {
                    "xsec_token": "LB456R5umDT_Rtp-4igflNm-Iy4ZsfLOu_Mx_Jz0GFPL4=",
                    "type": "note_info",
                    "id": "697dcbb9000000002102abfd",
                    "content": "终末地基建【完全毕业】是怎样的感觉？",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k031s0h6kksju0g4a5rrihke633l7vtupg?imageView2/2/w/1080/format/jpg",
                    "status": 0,
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k031s0h6kksju0g4a5rrihke633l7vtupg?imageView2/2/w/1080/format/jpg",
                        "width": 758,
                        "height": 1011
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "link": "xhsdiscover://item/discovery.697dcbb9000000002102abfd?type=video&sourceID=notifications&feedType=single&anchorCommentId=698fc83b000000000800e199&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    }
                },
                "liked": false,
                "time_flag": 0,
                "id": "7606518456971543308"
            },
            {
                "title": "评论了你的笔记",
                "liked": false,
                "track_type": "41",
                "id": "7606436818234939271",
                "type": "comment/item",
                "time": 1771011580,
                "score": 7606436818234939271,
                "user_info": {
                    "userid": "62fe5e15000000001200d57a",
                    "nickname": "Russell Crowe FanAccount",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31g4lcb81hu005onuboakhlbqlu832e8?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABqt3QVBh3f_0pUr4XkGouBDejAhnkkZYWW0-6CDogJT4="
                },
                "item_info": {
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k03170jo5na0o004a5rrihke633pagoeio?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "link": "xhsdiscover://item/discovery.66cdbe94000000001d019f0e?type=video&sourceID=notifications&feedType=single&anchorCommentId=698f7dfa000000000c017c4e&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "status": 0,
                    "xsec_token": "LBG-1wEKpQNDUy8gxB055Jiaq8ZDYywC9bTlXG48mNCPU=",
                    "type": "note_info",
                    "id": "66cdbe94000000001d019f0e",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k03170jo5na0o004a5rrihke633pagoeio?imageView2/2/w/1080/format/jpg",
                    "content": "黑神话悟空亢金龙怎么打？毫毛定身秒杀流",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    }
                },
                "comment_info": {
                    "illegal_info": {
                        "status": 1,
                        "desc": "原评论已删除",
                        "illegal_status": "DELETE"
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0,
                    "id": "698f7dfa000000000c017c4e",
                    "content": "根本不会飞过来倒地上[doge]"
                },
                "time_flag": 0
            },
            {
                "time": 1770968953,
                "score": 7606253736663725935,
                "user_info": {
                    "userid": "602395560000000001007350",
                    "nickname": "音起行",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1000g2jo2ikg5ttcio06g5o13ilb08sqg62uodcg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABfozpLsbifuuTDS-nYrUAXLpvONyfoLrJNczleIZx5nQ="
                },
                "comment_info": {
                    "content": "感谢！！！伤害高20s过",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0,
                    "liked": true,
                    "like_count": 1,
                    "id": "698ed776000000000c0163a1"
                },
                "liked": false,
                "id": "7606253736663725935",
                "type": "comment/item",
                "title": "评论了你的笔记",
                "item_info": {
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "status": 0,
                    "type": "note_info",
                    "id": "66d33d74000000001d01be71",
                    "link": "xhsdiscover://item/discovery.66d33d74000000001d01be71?type=video&sourceID=notifications&feedType=single&anchorCommentId=698ed776000000000c0163a1&authorId=5b11e34711be10479b461863",
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "xsec_token": "LBX9jsMB9hFlTSB30BM1P8hNLNdlQ6uPHvPhjTlWtQ1LU=",
                    "content": "黑神话悟空毒敌大王怎么打？一波流逃课打法",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k03175v93t50o004a5rrihke633f3ke1bo?imageView2/2/w/1080/format/jpg",
                    "image_info": {
                        "width": 1242,
                        "height": 1656,
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k03175v93t50o004a5rrihke633f3ke1bo?imageView2/2/w/1080/format/jpg"
                    }
                },
                "track_type": "41",
                "time_flag": 0
            },
            {
                "id": "7606011981544683875",
                "type": "comment/item",
                "title": "评论了你的笔记",
                "user_info": {
                    "userid": "552dc4a12e1d930ef8866d43",
                    "nickname": "weipeixiaoxiao",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/5f80626cb6a9920001c3d737.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABydqENadmg-oC_zcJLhGC3JouOvTGUFN3h0WvHKpxEEk="
                },
                "item_info": {
                    "content": "黑神话悟空高周目大圣怎么打？一套公式通解",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                    "link": "xhsdiscover://item/discovery.670d10120000000021005d8c?type=video&sourceID=notifications&feedType=single&anchorCommentId=698dfb97000000000601f57f&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "xsec_token": "LB-1wCwjd-goZ8UOfZg4U-QvXG36wGED7zBKYDlkO5ZN8=",
                    "type": "note_info",
                    "id": "670d10120000000021005d8c",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k0318ueds5ugo004a5rrihke633rdn49ug?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "status": 0
                },
                "time": 1770912665,
                "score": 7606011981544683875,
                "comment_info": {
                    "liked": false,
                    "like_count": 0,
                    "id": "698dfb97000000000601f57f",
                    "content": "我到了三中目，无量福根本动不住",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "status": 0
                },
                "track_type": "41",
                "liked": false,
                "time_flag": 0
            },
            {
                "comment_info": {
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0,
                    "target_comment": {
                        "illegal_info": {
                            "status": 0,
                            "desc": "",
                            "illegal_status": "NORMAL"
                        },
                        "user_info": {
                            "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                            "red_official_verify_type": 0,
                            "userid": "5b11e34711be10479b461863",
                            "nickname": "低配玩家小马"
                        },
                        "status": 0,
                        "liked": false,
                        "like_count": 0,
                        "id": "68a015d600000000260395cc",
                        "content": "分身是在黄风门口土地庙学"
                    },
                    "id": "698df5f4000000000c014c20",
                    "content": "？？分身不是在石敢当后面溜坡那"
                },
                "track_type": "40",
                "liked": false,
                "type": "comment/comment",
                "time": 1770911223,
                "score": 7606005788201359670,
                "item_info": {
                    "type": "note_info",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k0316tiu9740m004a5rrihke6332057bjg?imageView2/2/w/1080/format/jpg",
                    "link": "xhsdiscover://item/discovery.66caa65c000000001d03b297?type=video&sourceID=notifications&feedType=single&anchorCommentId=698df5f4000000000c014c20&authorId=5b11e34711be10479b461863",
                    "status": 0,
                    "id": "66caa65c000000001d03b297",
                    "content": "黑神话悟空无赖逃课打法，石先锋一招搞定",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k0316tiu9740m004a5rrihke6332057bjg?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1656
                    },
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    },
                    "xsec_token": "LBDqcqsYsDxWE2XFGwTapfXgBSJ1i-HlxgS05kacIHsEA="
                },
                "id": "7606005788201359670",
                "title": "回复了你的评论",
                "user_info": {
                    "userid": "5aafbbfc11be10346fcfe2f4",
                    "nickname": "momo",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/63d1cf83d890f354a7c30ef4.jpg?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABRSw_ELWDaIOCvESGTbnBTnx8oJ53JFJ_Wkh0j-mko2E="
                },
                "time_flag": 0
            },
            {
                "item_info": {
                    "xsec_token": "LB456R5umDT_Rtp-4igflNm-Iy4ZsfLOu_Mx_Jz0GFPL4=",
                    "type": "note_info",
                    "content": "终末地基建【完全毕业】是怎样的感觉？",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g0k031s0h6kksju0g4a5rrihke633l7vtupg?imageView2/2/w/1080/format/jpg",
                        "width": 758,
                        "height": 1011
                    },
                    "link": "xhsdiscover://item/discovery.697dcbb9000000002102abfd?type=video&sourceID=notifications&feedType=single&anchorCommentId=698d721d000000000600f9ff&authorId=5b11e34711be10479b461863",
                    "status": 0,
                    "id": "697dcbb9000000002102abfd",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g0k031s0h6kksju0g4a5rrihke633l7vtupg?imageView2/2/w/1080/format/jpg",
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "user_info": {
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0
                    }
                },
                "track_type": "41",
                "liked": false,
                "time_flag": 0,
                "time": 1770877474,
                "score": 7605860837350671909,
                "title": "评论了你的笔记",
                "user_info": {
                    "userid": "602b1eea000000000100b022",
                    "nickname": "枝头",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31cv3s0jlh25g5o1b3rl09c12p53dhog?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "AB83W8slL3qkjwD9SfoPfXlYMUjN2I4dO8Dr-4ftcHFec="
                },
                "comment_info": {
                    "status": 0,
                    "liked": false,
                    "like_count": 0,
                    "id": "698d721d000000000600f9ff",
                    "content": "不怎么样，不想玩了",
                    "illegal_info": {
                        "illegal_status": "NORMAL",
                        "status": 0,
                        "desc": ""
                    }
                },
                "id": "7605860837350671909",
                "type": "comment/item"
            },
            {
                "id": "7605572378756413458",
                "type": "comment/item",
                "time": 1770810312,
                "user_info": {
                    "userid": "6296cba4000000002102069b",
                    "nickname": "一只小花",
                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31slcqgj2m26g5okmpei8c1krbnmrbd0?imageView2/2/w/120/format/jpg",
                    "red_official_verify_type": 0,
                    "xsec_token": "ABoqI5wHyQ-RXVAhgAP769t7X7mE8oboR2hXKieNMLw4c="
                },
                "comment_info": {
                    "id": "698c6bc4000000000d0112ec",
                    "content": "还愿了主播",
                    "illegal_info": {
                        "desc": "",
                        "illegal_status": "NORMAL",
                        "status": 0
                    },
                    "status": 0,
                    "liked": false,
                    "like_count": 0
                },
                "track_type": "41",
                "liked": false,
                "time_flag": 0,
                "title": "评论了你的笔记",
                "score": 7605572378756413458,
                "item_info": {
                    "status": 0,
                    "xsec_token": "LB_k0EwC818wqnwEcHlN99sDY-UTNyZkDzI2l2is8FjWg=",
                    "image_info": {
                        "url": "http://ci.xiaohongshu.com/spectrum/1040g34o3178bo0kijk0g4a5rrihke633avgrkog?imageView2/2/w/1080/format/jpg",
                        "width": 1242,
                        "height": 1660
                    },
                    "illegal_info": {
                        "status": 0,
                        "desc": "",
                        "illegal_status": "NORMAL"
                    },
                    "link": "xhsdiscover://item/discovery.66d5ae6f000000001d018bd2?type=video&sourceID=notifications&feedType=single&anchorCommentId=698c6bc4000000000d0112ec&authorId=5b11e34711be10479b461863",
                    "user_info": {
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo316r0inu2k40g4a5rrihke633g210pbo?imageView2/2/w/120/format/jpg",
                        "red_official_verify_type": 0,
                        "userid": "5b11e34711be10479b461863",
                        "nickname": "低配玩家小马"
                    },
                    "type": "note_info",
                    "id": "66d5ae6f000000001d018bd2",
                    "content": "黑神话悟空晦月魔君怎么打？全网最简单打法",
                    "image": "http://ci.xiaohongshu.com/spectrum/1040g34o3178bo0kijk0g4a5rrihke633avgrkog?imageView2/2/w/1080/format/jpg"
                }
            }
        ],
        "has_more": true,
        "cursor": 7605572378756413458
    },
    "code": 0
}
```