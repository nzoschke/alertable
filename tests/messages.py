from google.appengine.api.mail import EmailMessage, InboundEmailMessage

sms1 = InboundEmailMessage("""Delivered-To: joe@example.com
Received: by 10.229.75.8 with SMTP id w8cs468682qcj;
       Sat, 27 Feb 2010 16:53:46 -0800 (PST)
Return-Path: <3mb6JSyIUAC0kmlmljpppln.krkrokololj.ouk6AnSZ-Pcgc.eXRLN.PXXPUN.LXV@grandcentral.bounces.google.com>
Received-SPF: pass (google.com: domain of 3mb6JSyIUAC0kmlmljpppln.krkrokololj.ouk6AnSZ-Pcgc.eXRLN.PXXPUN.LXV@grandcentral.bounces.google.com designates 10.231.144.12 as permitted sender) client-ip=10.231.144.12;
Authentication-Results: mr.google.com; spf=pass (google.com: domain of 3mb6JSyIUAC0kmlmljpppln.krkrokololj.ouk6AnSZ-Pcgc.eXRLN.PXXPUN.LXV@grandcentral.bounces.google.com designates 10.231.144.12 as permitted sender) smtp.mail=3mb6JSyIUAC0kmlmljpppln.krkrokololj.ouk6AnSZ-Pcgc.eXRLN.PXXPUN.LXV@grandcentral.bounces.google.com; dkim=pass header.i=3mb6JSyIUAC0kmlmljpppln.krkrokololj.ouk6AnSZ-Pcgc.eXRLN.PXXPUN.LXV@grandcentral.bounces.google.com
Received: from mr.google.com ([10.231.144.12])
       by 10.231.144.12 with SMTP id x12mr212260ibu.10.1267318425613 (num_hops = 1);
       Sat, 27 Feb 2010 16:53:45 -0800 (PST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
       d=google.com; s=beta;
       h=domainkey-signature:mime-version:received:message-id:date:subject
        :from:to:content-type;
       bh=EtcAwegA7XEyCD6yEF4DBfmfWY0wDTCbHHm/TKENUUE=;
       b=kQtX9jbpPuJS7Cse6lfRQUqVNMn1NPTTPUPGzTXlKyWWaMOCjkaKAuH3yZ+QbxPl+Y
        9uQs8PK/vbEWlQgXQ8Aw==
DomainKey-Signature: a=rsa-sha1; c=nofws;
       d=google.com; s=beta;
       h=mime-version:message-id:date:subject:from:to:content-type;
       b=Y/mF1chMsciQaRtSzYwh66x3qFka5qKu1m6MwXayzSThmqzcG0iNTV6PQXRfEa1IxU
        MCUX1ls5RzdzfUzbSY7Q==
MIME-Version: 1.0
Received: by 10.231.144.12 with SMTP id x12mr180422ibu.10.1267318425588; Sat, 
	27 Feb 2010 16:53:45 -0800 (PST)
Message-ID: <+15555551212.5d7e59091c3ddc6a318217974d5dfb54a9821f1f@txt.voice.google.com>
Date: Sun, 28 Feb 2010 00:53:45 +0000
Subject: SMS from Mr. Ed [(555) 555-1212]
From: "Mr. Ed (SMS)" <15555551212.15558675309.5B1NR4jq-g@txt.voice.google.com>
To: joe@example.com
Content-Type: text/plain; charset=ISO-8859-1; format=flowed; delsp=yes

What time is the show?
I - can't remember

--
Sent using SMS-to-email.  Reply to this email to text the sender back and  
save on SMS fees.
https://www.google.com/voice
""")

sms2 = InboundEmailMessage("""Delivered-To: joe@example.com
Received: by 10.229.75.8 with SMTP id w8cs476219qcj;
        Sat, 27 Feb 2010 21:34:50 -0800 (PST)
Return-Path: <3eQCKSyIUAE8IKJKJHNNNJL.IPIPMIMJMJH.MSIeiL07-xAEA.C5ztv.x55x2v.t53@grandcentral.bounces.google.com>
Received-SPF: pass (google.com: domain of 3eQCKSyIUAE8IKJKJHNNNJL.IPIPMIMJMJH.MSIeiL07-xAEA.C5ztv.x55x2v.t53@grandcentral.bounces.google.com designates 10.231.168.197 as permitted sender) client-ip=10.231.168.197;
Authentication-Results: mr.google.com; spf=pass (google.com: domain of 3eQCKSyIUAE8IKJKJHNNNJL.IPIPMIMJMJH.MSIeiL07-xAEA.C5ztv.x55x2v.t53@grandcentral.bounces.google.com designates 10.231.168.197 as permitted sender) smtp.mail=3eQCKSyIUAE8IKJKJHNNNJL.IPIPMIMJMJH.MSIeiL07-xAEA.C5ztv.x55x2v.t53@grandcentral.bounces.google.com; dkim=pass header.i=3eQCKSyIUAE8IKJKJHNNNJL.IPIPMIMJMJH.MSIeiL07-xAEA.C5ztv.x55x2v.t53@grandcentral.bounces.google.com
Received: from mr.google.com ([10.231.168.197])
        by 10.231.168.197 with SMTP id v5mr246261iby.27.1267335289973 (num_hops = 1);
        Sat, 27 Feb 2010 21:34:49 -0800 (PST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=google.com; s=beta;
        h=domainkey-signature:mime-version:references:received:message-id
         :date:subject:from:to:content-type;
        bh=14JDXtIm0uvGyhqBB7i6JVJEjMCb5INjl/hP1peaFJU=;
        b=Tq3GzsEVDmm6K7MrsnRZew3BL+VC7xGEfif8PoT3QaKueGbeIpLGsBujr0RtSKzwRO
         7apD52CRZVLXnjUnE+NQ==
DomainKey-Signature: a=rsa-sha1; c=nofws;
        d=google.com; s=beta;
        h=mime-version:references:message-id:date:subject:from:to
         :content-type;
        b=B5wbbATmuQI9k+MuKSHc/dDfv7cow709djC6rv+aJGkDobSNKwqkrr/eHnRsHXMdQ1
         pd+DDqQbafuk1FX6rhYA==
MIME-Version: 1.0
References: <+15555551212.5d7e59091c3ddc6a318217974d5dfb54a9821f1f@txt.voice.google.com>
Received: by 10.231.168.197 with SMTP id v5mr205127iby.27.1267335289951; Sat, 
	27 Feb 2010 21:34:49 -0800 (PST)
Message-ID: <+15555551212.bf2bfd0267caafa847843d41bebc1c6ecc0a5203@txt.voice.google.com>
Date: Sun, 28 Feb 2010 05:34:49 +0000
Subject: SMS from Mr. Ed [(555) 555-1212]
From: "Mr. Ed (SMS)" <15555551212.15558675309.5B1NR4jq-g@txt.voice.google.com>
To: joe@example.com
Content-Type: text/plain; charset=ISO-8859-1; format=flowed; delsp=yes

Ok I will see you at 8""")

vm = InboundEmailMessage("""Delivered-To: joe@example.com
Received: by 10.229.75.8 with SMTP id w8cs412072qcj;
        Fri, 26 Feb 2010 16:21:22 -0800 (PST)
Return-Path: <3gWWISw0KCLo0tnhj-stwjuq3lttlqj.htrs4txhmpjlrfnq.htr@grandcentral.bounces.google.com>
Received-SPF: pass (google.com: domain of 3gWWISw0KCLo0tnhj-stwjuq3lttlqj.htrs4txhmpjlrfnq.htr@grandcentral.bounces.google.com designates 10.90.41.23 as permitted sender) client-ip=10.90.41.23;
Authentication-Results: mr.google.com; spf=pass (google.com: domain of 3gWWISw0KCLo0tnhj-stwjuq3lttlqj.htrs4txhmpjlrfnq.htr@grandcentral.bounces.google.com designates 10.90.41.23 as permitted sender) smtp.mail=3gWWISw0KCLo0tnhj-stwjuq3lttlqj.htrs4txhmpjlrfnq.htr@grandcentral.bounces.google.com; dkim=pass header.i=3gWWISw0KCLo0tnhj-stwjuq3lttlqj.htrs4txhmpjlrfnq.htr@grandcentral.bounces.google.com
Received: from mr.google.com ([10.90.41.23])
        by 10.90.41.23 with SMTP id o23mr1650083ago.7.1267230081534 (num_hops = 1);
        Fri, 26 Feb 2010 16:21:21 -0800 (PST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=google.com; s=beta;
        h=domainkey-signature:mime-version:received:message-id:date:subject
         :from:to:content-type;
        bh=bP3OYwSCdrwyBoSk7WWSJfrns2p7zkI3xAH9Q7OVWJY=;
        b=fd69UAKMwPuTebfcXFtXyIQKWXDzUx6US5LFcxBvMzhsGY5uvRlixu32JQM/mxHPBP
         ix45voPwfOCjHWofN28w==
DomainKey-Signature: a=rsa-sha1; c=nofws;
        d=google.com; s=beta;
        h=mime-version:message-id:date:subject:from:to:content-type;
        b=UcPdGcxizC8tRL56zxxGGNjHmoMX+Mg3RDFacKDH21wC2HnBSyKA3cTLrwsptlcrhU
         8GcAhcysu4fQzGFxyv3Q==
MIME-Version: 1.0
Received: by 10.90.41.23 with SMTP id o23mr1296184ago.7.1267230081504; Fri, 26 
	Feb 2010 16:21:21 -0800 (PST)
Message-ID: <0016362838c6db55eb048089feb0@google.com>
Date: Sat, 27 Feb 2010 00:21:21 +0000
Subject: New voicemail from Mr Wizard at 4:19 PM
From: Google Voice <voice-noreply@google.com>
To: joe@example.com
Content-Type: multipart/alternative; boundary=0016362838c6db55d7048089fead

--0016362838c6db55d7048089fead
Content-Type: text/plain; charset=ISO-8859-1; format=flowed; delsp=yes

Voicemail from Mr Wizard (555) 555-1212 at 4:19 PM
Transcript: Call me back. Bye.
Play message:  
https://www.google.com/voice/fm/17115525943858205198/AHwOX_BKNy61yqK24tiPRLdY0lU1Yd0BohgzPKxl9D7dI0I6FuWEdJWAabXViBfUraOww6AdpnprnymdMNoanFF9vuRysdrRyD4HiWtAUIdrozaNFl4oA62_KgEUo_ow5CYgcx-hV94stXCXTMF2RhggtZNdjE5Pqw

You have 2 Google Voice invites left. Invite a friend (  
https://www.google.com/voice/account/signin/?prev=%2F%23invite%2F );

--0016362838c6db55d7048089fead
Content-Type: text/html; charset=ISO-8859-1
Content-Transfer-Encoding: quoted-printable

<table cellpadding=3D"2" border=3D"0" width=3D"620" style=3D"border-collaps=
e:collapse;">
  <tr>
    <td valign=3D"bottom">
      <div style=3D"font-size: 120%; padding-left: 4px;"> Voicemail from: <=
b>Mr Wizard</b> (928) 200-1092 at 4:19 PM</div>
    </td>
    <td align=3D"right"><a href=3D"https://www.google.com/voice/"><img src=
=3D"https://www.google.com/voice/static/voice_logo_sm2.png" alt=3D"Google V=
oice" width=3D"122" height=3D"30" border=3D"0"/></a></td>
  </tr>
  <tr>
    <td colspan=3D"2">
      <div style=3D"border: #c0cde5 solid 1px; background-color: #e8eef7; p=
adding: 10px; line-height: 140%">
        <span style=3D"color:#000;">Call </span><span style=3D"color:#888;">=
me</span><span style=3D"color:#888;">back.</span><span style=3D"col=
or:#888;">Bye. </span>
        <br/>
        <a href=3D"https://www.google.com/voice/fm/...">Play message</a>
        </div>
    </td>
  </tr>
 =20
  <tr>
    <td><div style=3D"color: #808080; margin-left: 4px;"> You have 2 Google=
 Voice invites left. <a href=3D"https://www.google.com/voice/account/signin=
/?prev=3D%2F%23invite%2F">Invite a friend &#0187;</a></div></td>
  </tr>
 =20
</table>
--0016362838c6db55d7048089fead--""")