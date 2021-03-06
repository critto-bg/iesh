# -*-python-*-
# ie_shell.py - Simple shell for Infinity Engine-based game files
# Copyright (C) 2004-2008 by Jaroslav Benkovsky, <edheldil@users.sf.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


# FIXME: add descriptions to the options

options = {
    'core.chitin_file': ['CHITIN.KEY', ""],
    'core.dialog_file': ['dialog.tlk', ""],
    'pager': ['more', "Program to use for paging command output"],
    'use_cache': [True, "Cache open BIF files"],
    'encoding': [None, "Encoding used for printing strings, e.g. 'utf8'"],

    'stream.debug_coverage': [False, "On stream close print info on offsets not read or read more than once"],
    'format.debug_read': [False, "Print each read op to stdout"],
    'format.debug_write': [False, "Print each write op to stdout"],
    'format.print_offset': [False, "Print field's offset"],
    'format.print_size': [False, "Print field's size (in bytes)"],
    'format.print_type': [False, "Print field's type"],

    #'format.bam.force_rle': [True,  "Assume that frame data is always RLE encoded"],
    'format.bam.decode_frame_data': [True, "Decode BAM frame data"],
    'format.bam.print_frame_bitmap': [True, "Print BAM frame data"],
    'format.bam.print_palette': [True, "Print BAM frame palette" ],

    'format.biff.read_data': [False,  "When reading BIFF file read its data too"],

    'format.bmp.print_bitmap': [True, "Print BMP bitmap"],
    'format.bmp.print_palette': [True, "Print BMP palette" ],

    'format.key.tick_size': [ 100, "# of RESREFs read to print a dot" ],
    'format.key.tack_size': [ 5000, "# of RESREFs read to print a number" ],
    'format.key.max_read_resrefs': [None,  "Max # of RESREFs to read from KEY file"],

    'format.mos.print_tiles': [True,  "Print MOS tiles"],
    'format.mos.print_palettes': [False,  "Print MOS palettes"],

    'format.plt.print_bitmap': [True, "Print PLT bitmap"],

    'format.sav.read_data': [False,  "When reading SAV file read its data too"],

    'format.tis.print_tiles': [False,  "Print TIS tiles"],
    'format.tis.print_palettes': [False,  "Print TIS palettes"],

    'format.tlk.tick_size': [ 100, "# of STRREFs read to print a dot" ],
    'format.tlk.tack_size': [ 5000, "# of STRREFs read to print a number" ],
    'format.tlk.decode_strrefs': [True,  "Read TLK strrefs, not only header"],
    'format.tlk.encoding': [None, "Encoding of strings in game data, e.g. cp1250 (Czech), cp932 (Japanese), cp949 (Korean), cp950 (Chinese)"],
    #src_enc = 'cp1250' # Czech
    #src_enc = 'cp949' # Korean, but some strings are in French
    #src_enc = 'cp932' # Japanese
    #src_enc = 'cp950' # Chinese
}

# these are borrowed from WeiDU
# FIXME: when consensus is reached on how to detected SoD, support should be added
game_types = {
    'bg1':   ("AR0125",   "ARE"),
    'bg1ee': ("OH1000",   "ARE"),
    'bg2':   ("AR0083",   "ARE"),
    'tob':   ("AR6111",   "ARE"),
    'bg2ee': ("OH6000",   "ARE"),
    'iwd':   ("AR2116",   "ARE"),
    'how':   ("AR9109",   "ARE"),
    'iwdee': ("HOWPARTY", "2DA"),
    'iwd2':  ("AR6050",   "ARE"),
    'pst':   ("AR0104A",  "ARE"),
}

game_type_weights = {
    'bg1'  : 90,
    'bg1ee': 100,
    'bg2'  : 80,
    'tob'  : 90,
    'bg2ee': 100,
    'iwd'  : 90,
    'how'  : 100,
    'iwdee': 100,
    'iwd2' : 100,
    'pst'  : 100
}

# End of file defaults.py
