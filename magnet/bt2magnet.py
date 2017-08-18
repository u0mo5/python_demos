#! /usr/local/bin/python
# @desc python
# @date 2015/11/10
# @author pythontab.com
import bencode
import sys
import hashlib
import base64
import urllib
#
torrentName = sys.argv[1]
#
torrent = open(torrentName, 'rb').read()
#
metadata = bencode.bdecode(torrent)
hashcontents = bencode.bencode(metadata['info'])
digest = hashlib.sha1(hashcontents).digest()
b32hash = base64.b32encode(digest)
#
print 'magnet:?xt=urn:btih:%s' % b32hash