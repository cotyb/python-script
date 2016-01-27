#coding="utf-8"
fp = open("get_flow_table.sh","w")
for i in range(1,17):
    print >> fp, "curl http://192.168.29.246:8080/stats/flow/%s >> flows/s%s_flow" %(i,i)

for i in range(1000,1010):
    print >> fp, "curl http://192.168.29.246:8080/stats/flow/%s >> flows/s%s_flow" %(i,i)

fp.close()
