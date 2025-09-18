## Test VIF and VLANs
NDC01 - VLAN 1301 - 169.254.51.0/30
NDC02 - VLAN 1302 - 169.254.52.0/30
CDC01 - VLAN 1303 - 169.254.53.0/30
CDC02 - VLAN 1304 - 169.254.54.0/30


running BFD sessions using the commands below

'no ip redirects '
'no ipv6 redirects '

Please configure relaxed BFD intervals when scaling above a total of 128 BFD sessions
on Cloudscale platforms and Silicon One platforms using the commands below

'bfd interval 300 min_rx 300 multiplier 3'
'bfd multihop interval 999 min_rx 999 multiplier 10'



2025 Jul 17 10:55:19 WBGF01-N9K-C93180YC-FX001 %BFD-5-SESSION_MOVED: BFD session 0x41000001: Installed on LC 1
2025 Jul 17 10:55:19 WBGF01-N9K-C93180YC-FX001 %BFD-5-SESSION_CREATED: BFD session to neighbor 169.254.32.2 on interface Vlan100 has been created
2025 Jul 17 10:55:28 WBGF01-N9K-C93180YC-FX001 %BFD-5-SESSION_STATE_UP: BFD session 1090519041 to neighbor 169.254.32.2 on interface Vlan100 is up.

INC 44259200