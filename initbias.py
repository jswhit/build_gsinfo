#  read(lunin,'(I5,1x,A20,1x,I5,2e15.6,1x,I5/2(4x,10f12.6/))',iostat=istat,end=1333)
#  ich,isis,ichan,tlapm,tsum,ntlapupdate,(predr(ip),ip=1,npred)
# open old satbias file
import sys
fin = sys.argv[1] # read satinfo
fout = 'bias'
fout2= 'bias_pc'
f = open(fin); fo = open(fout,'w'); fo2 = open(fout2,'w')
ich = 1
for line in f:
    if line.startswith('!'): 
        continue
    linesplit = line.split()
    isis = linesplit[0].lstrip()
    ichan = int(linesplit[1])
    fo.write('%5i %-20s %5i   0.000000E+00   0.000000E+00     0\n' % (ich,isis,ichan))
    fo.write('        0.000000    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000\n')
    fo.write('        0.000000    0.000000\n')
    fo2.write('%5i %-20s %5i   0.000000E+00\n' % (ich,isis,ichan))
    fo2.write('      1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05  1.0000000E+05\n')
    fo2.write('      1.0000000E+05  1.0000000E+05\n')
    #fo2.write('      0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00\n')
    #fo2.write('      0.0000000E+00  0.0000000E+00\n')
    ich += 1
f.close()
fo.close()
fo2.close()
