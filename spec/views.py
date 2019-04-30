# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.shortcuts import render

# from django.shortcuts import HttpResponse

# Create your views here.
requestPerTabelName = ''
requestPerList = []
LPerId = ''
PerIdUnit = ''
LPerPrimId = ''
PerXXXCur = {'name': '', 'data': ''}
PerXXXHis = {'name': '', 'data': ''}
neBase = ''
PerObjTypeList = ''
DataTypeDef = ''
LDataType = ''
LPerFb = ''
XXXWs = ''
perToolsCpp = ''
perToolsH = ''
toolFidCpp = ''
MtnCmdDcCpp = ''
NESvcCfgPerMonitorCfgCpp = ''
NeSvcCommDataDecomposeCpp = ''
NeSvcCommDataMtnCpp = ''
NeSvcCfgLgCfgMngCpp = ''
perChssHelperCpp = ''
perChssModCpp = ''
perChssModH = ''
perNeModCpp = ''
perNeModH = ''
CMakeListsTxt = ''
cliApiAlarmperCPP = ''
cliApiAlarmperH = ''
cliCmdMoncmmCpp = ''
cliCmdSysCpp = ''

def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("hello world!")
    global requestPerTabelName, requestPerList, LPerId, PerIdUnit, LPerPrimId, PerXXXCur, PerXXXHis, neBase,\
        PerObjTypeList, DataTypeDef, LDataType, LPerFb, XXXWs, perToolsCpp, perToolsH, toolFidCpp, MtnCmdDcCpp, \
        NESvcCfgPerMonitorCfgCpp, NeSvcCommDataDecomposeCpp, NeSvcCommDataMtnCpp, NeSvcCfgLgCfgMngCpp,\
        perChssHelperCpp, perChssModCpp, perChssModH, perNeModCpp, perNeModH, CMakeListsTxt, cliApiAlarmperCPP,\
        cliApiAlarmperH, cliCmdMoncmmCpp, cliCmdSysCpp
    requestPerList = []
    LPerId = ''
    PerIdUnit = ''
    LPerPrimId = ''
    PerXXXCur = {'name': '', 'data': ''}
    PerXXXHis = {'name': '', 'data': ''}


    if request.method == 'POST':

        requestPerTabelName = request.POST.get('requestPerTabelName', None)
        requestPerTabelId = request.POST.get('requestPerTabelId', None)
        requestPerName = request.POST.get('requestPerName', None)
        requestPerId = request.POST.get('requestPerId', None)
        requestPrimId = request.POST.get('requestPrimId', None)
        requestPerNameListTemp = re.split("[_/\\\\,.\-;:`~|<> ]", requestPerName)
        requestPerNameListTemp = filter(None, requestPerNameListTemp)  # 去除空值
        if (re.search(r'[~-]', requestPerId)):
            requestPerIdRange = re.split("[~-]", requestPerId)
            requestPerIdListTemp = range(int(requestPerIdRange[0]), int(requestPerIdRange[1]) + 1)
        else:
            requestPerIdListTemp = re.split("[_/\\\\,.\;:`|<> ]", requestPerId)
        requestPerIdListTemp = filter(None, requestPerIdListTemp)  # 去除空值
        if (requestPrimId == ''):
            requestPrimId = requestPerId
        if (re.search(r'[~-]', requestPrimId)):
            requestPrimIdRange = re.split("[~-]", requestPrimId)
            requestPrimIdListTemp = range(int(requestPrimIdRange[0]), int(requestPrimIdRange[1]) + 1)
        else:
            requestPrimIdListTemp = re.split("[_/\\\\,.\;:`|<> ]", requestPrimId)
        requestPrimIdListTemp = filter(None, requestPrimIdListTemp)  # 去除空值

        setPerXXXCurStart(PerXXXCur, requestPerTabelName)
        setPerXXXHisStart(PerXXXHis, requestPerTabelName)
        neBase = getNeBaseOtrStart(requestPerTabelName)
        PerObjTypeList = getPerObjTypeList(requestPerTabelName, requestPerTabelId)
        DataTypeDef = getDataTypeDef()
        LDataType = getLDataType()
        LPerFb = getLPerFb(requestPerTabelName, requestPerTabelId)
        XXXWs = getXXXWs()

        for requestPerNameTemp, requestPerIdTemp, requestPrimIdTemp in zip(requestPerNameListTemp, requestPerIdListTemp, requestPrimIdListTemp):
            requestPerList.append({'name': requestPerNameTemp, 'id': requestPerIdTemp, 'primId': requestPrimIdTemp})
            LPerId += getLPerId(requestPerIdTemp, requestPerNameTemp)
            PerIdUnit += getPerIdUnit(requestPerIdTemp)
            LPerPrimId += getLPerPrimId(requestPrimIdTemp, requestPerNameTemp)
            PerXXXCur['data'] += getPerXXXCurData(requestPerNameTemp)
            PerXXXHis['data'] += getPerXXXHisData(requestPerNameTemp)
            neBase += getNeBaseOtrData(requestPerNameTemp)

        neBase += getNeBaseOtrEnd(requestPerTabelName)
        setPerXXXCurEnd(PerXXXCur)
        setPerXXXHisEnd(PerXXXHis)

        perToolsCpp = getPerToolsCpp(requestPerTabelName, requestPerTabelId, requestPerNameListTemp)
        perToolsH = getPerToolsH(requestPerTabelName, requestPerNameListTemp)
        toolFidCpp = getToolFidCpp(requestPerTabelName)
        MtnCmdDcCpp = getMtnCmdDcCpp(requestPerTabelName)
        NESvcCfgPerMonitorCfgCpp = getNESvcCfgPerMonitorCfgCpp(requestPerTabelName)
        NeSvcCommDataDecomposeCpp = getNeSvcCommDataDecomposeCpp(requestPerTabelName)
        NeSvcCommDataMtnCpp = getNeSvcCommDataMtnCpp(requestPerTabelName)
        NeSvcCfgLgCfgMngCpp = getNeSvcCfgLgCfgMngCpp(requestPerTabelName)
        perChssHelperCpp = getPerChssHelperCpp(requestPerTabelName)
        perChssModCpp = getPerChssModCpp(requestPerTabelName, requestPerTabelId)
        perChssModH = getPerChssModH(requestPerTabelName, requestPerTabelId)
        perNeModCpp = getPerNeModCpp(requestPerTabelName, requestPerNameListTemp)
        perNeModH = getPerNeModH(requestPerTabelName)
        CMakeListsTxt = getCMakeListsTxt(requestPerTabelName)
        cliApiAlarmperCPP = getCliApiAlarmperCPP(requestPerTabelName, requestPerNameListTemp)
        cliApiAlarmperH = getCliApiAlarmperH(requestPerTabelName, requestPerNameListTemp)
        cliCmdMoncmmCpp = getCliCmdMoncmmCpp(requestPerTabelName, requestPerNameListTemp)
        cliCmdSysCpp = getCliCmdSysCpp(requestPerTabelName)

    return render(request, "index.html", {'tableName': requestPerTabelName, 'data': requestPerList, 'LperIdTd': LPerId,
                                          'PerIdUnitTd': PerIdUnit, 'LPerPrimIdTd': LPerPrimId,
                                          'PerXXXCurTd': PerXXXCur, 'PerXXXHisTd': PerXXXHis,
                                          'neBaseOtrXml': neBase, 'PerObjTypeList': PerObjTypeList,
                                          'DataTypeDef': DataTypeDef, 'LDataType': LDataType,
                                          'LPerFb': LPerFb, 'XXXWs': XXXWs,
                                          'perToolsCpp': perToolsCpp, 'perToolsH': perToolsH,
                                          'toolFidCpp': toolFidCpp, 'MtnCmdDcCpp': MtnCmdDcCpp,
                                          'NESvcCfgPerMonitorCfgCpp': NESvcCfgPerMonitorCfgCpp,
                                          'NeSvcCommDataDecomposeCpp': NeSvcCommDataDecomposeCpp,
                                          'NeSvcCommDataMtnCpp': NeSvcCommDataMtnCpp,
                                          'NeSvcCfgLgCfgMngCpp': NeSvcCfgLgCfgMngCpp,
                                          'perChssHelperCpp': perChssHelperCpp,
                                          'perChssModCpp': perChssModCpp, 'perChssModH': perChssModH,
                                          'perNeModCpp': perNeModCpp, 'perNeModH': perNeModH,
                                          'CMakeListsTxt': CMakeListsTxt,
                                          'cliApiAlarmperCPP': cliApiAlarmperCPP, 'cliApiAlarmperH': cliApiAlarmperH,
                                          'cliCmdMoncmmCpp': cliCmdMoncmmCpp, 'cliCmdSysCpp': cliCmdSysCpp})


def getCliCmdSysCpp(requestPerTabelName):
    return '''
void PerObjTypeToStr(Long PerObjType, char out[])
{
	switch(PerObjType)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		sprintf(out,"''' + requestPerTabelName.lower() + '''");
		break;
	}
}'''

def getCliCmdMoncmmCpp(requestPerTabelName, requestPerNameList):
    outString = '''
IdNameNode perTypeList[] = 
{
	IdNameNode(PerObjTypeList_''' + requestPerTabelName.lower() + ''',"''' + requestPerTabelName.lower() + '''"),
};

/////////////////////////////

IdNameNode perIdNameList[] = 
{
	IdNameNode(LPerId_''' + requestPerNameList[0] + ''', "''' + requestPerNameList[0].lower() + '''"),  //ptppacket'''
    for requestPerNameTemp in requestPerNameList[1:]:
        outString += '''
	IdNameNode(LPerId_''' + requestPerNameTemp + ''', "''' + requestPerNameTemp.lower() + '''"),'''

    outString += '''
};

/////////////////////////////

int show_counters (struct utons_cli *cli, int argc, char **argv)//TODO
{
	else if((argc > arcindex + 3) && (0 == strcmp(argv[arcindex + 3], "''' + requestPerTabelName.lower() + '''")))
	{
		SEQUENCE<per_''' + requestPerTabelName.lower() + '''_cur> per_''' + requestPerTabelName.lower() + '''_list;
		SEQUENCE<per_''' + requestPerTabelName.lower() + '''_his> per_''' + requestPerTabelName.lower() + '''_his_list;
		
		if(isall)
		{
			sprintf(expression, "Fid='\\\\\\\\\\\\索引=%s'", argv[arcindex+1]);   //TODO:实现索引
			per_counters_get(per_''' + requestPerTabelName.lower() + '''_list, expression);
			per_his_counters_get(per_''' + requestPerTabelName.lower() + '''_his_list, expression);
		}
		else if(iscurrent)
		{
			sprintf(expression, "Fid='\\\\\\\\\\\\索引=%s' AND period=%d", argv[arcindex+1], period);   //TODO:实现索引
			per_counters_get(per_''' + requestPerTabelName.lower() + '''_list, expression);			
		}
		else
		{
			//hisnum--;
			sprintf(expression, "Fid='\\\\\\\\\\\\索引=%s' AND period=%d AND IdxNum=%d", argv[arcindex+1], period, hisnum);   //TODO:实现索引
			per_his_counters_get(per_''' + requestPerTabelName.lower() + '''_his_list, expression);
		}


		//! 打印输出.
		for (i = 0; i < per_''' + requestPerTabelName.lower() + '''_list.Length(); i++)
		{		
			dispString = per_''' + requestPerTabelName.lower() + '''_list[i].FormatInfo();
			utons_cli_out(cli,"%s\\n", (const char*)dispString);
			if(dispString)
			{
				NOICore::StringFree(dispString);
				dispString = NULL;
			}				
		}

		for (i = 0; i < per_''' + requestPerTabelName.lower() + '''_his_list.Length(); i++)
		{		
			dispString = per_''' + requestPerTabelName.lower() + '''_his_list[i].FormatInfo();
			utons_cli_out(cli,"%s\\n", (const char*)dispString);
			if(dispString)
			{
				NOICore::StringFree(dispString);
				dispString = NULL;
			}				
		}

		per_''' + requestPerTabelName.lower() + '''_list.ObjSetLength(0);
		per_''' + requestPerTabelName.lower() + '''_his_list.ObjSetLength(0);
	}
}

////////////////////////////////

char *show_counters_help[] =
{
"索引",   //TODO:实现索引
"索引值",   //TODO:实现索引值
"Object type",
"''' + requestPerTabelName.lower() + ''' performance",
};

////////////////////////////////
struct utons_cli_element show_counters_cli =
{
	"(索引 <索引值> type ''' + requestPerTabelName.lower() + ''') |" //实现索引
};

//////////////////////////////////

int set_performance_monitor (struct utons_cli *cli, int argc, char **argv)
{
		else if(0 == strcmp(argv[3], "''' + requestPerTabelName.lower() + '''"))
		{
			pertype = PerObjTypeList_''' + requestPerTabelName.lower() + ''';

			//添加性能基元设置选项
			if (0 == strcmp(argv[5], "all"))   
			{
				openAllItemFlag = 1;
			}
			
			if (0 == strcmp(argv[5], "''' + requestPerNameList[0].lower() + '''"))
			{
			    perId = (Short)(IdNameNode::QueryId(argv[5],perIdNameList));
			}'''
    for requestPerNameTemp in requestPerNameList[1:]:
        outString +='''
			else if (0 == strcmp(argv[5], "''' + requestPerNameTemp.lower() + '''"))
			{
			    perId = (Short)(IdNameNode::QueryId(argv[5],perIdNameList));
			}'''

    outString += '''
		}

		if (0 == strcmp(argv[6], "period"))
		{
			if (0 == strcmp(argv[7], "all"))
			{
				per15minFlag = 1;
				per24hFlag = 1;
			}
			else if (0 == strcmp(argv[7], "15min"))
			{
				per15minFlag = 1;

			}
			else if (0 == strcmp(argv[7], "24h"))
			{
				per24hFlag = 1;
			}

			if(0 == strcmp(argv[8], "on"))
			{
				ismonitor = 1;
			}
			else if(0 == strcmp(argv[8], "off"))
			{
				ismonitor = 0;
			}
		}
		else if (0 == strcmp(argv[6], "random"))
		{
			randomPeriod = (Short)atoi(argv[7]);

			if(0 == strcmp(argv[8], "on"))
			{
				isRandomMon = 1;
			}
			else if(0 == strcmp(argv[8], "off"))
			{
				isRandomMon = 0;
			}
		}
		sprintf(fid, "\\\\\\\\\\\\索引=%s", argv[1]);
		sprintf(expression,"Fid='%s' AND PerId= %d AND PerType = %d", (const char*)fid, perId, pertype);

    //............

	if (1 == openAllItemFlag)  //设置性能对象所有性能基元，即item设置参数选择了all
	{
			NSPASSERT(pertype >= PerObjTypeList_soh && pertype <= PerObjTypeList_''' + requestPerTabelName.lower() + ''');
	}
}

/////////////////////////////////

char *set_performance_monitor_help[] =
{
	"索引",		   //''' + requestPerTabelName.lower() + '''    //TODO:实现索引
	"索引值",  //TODO:实现索引值
	"Object type",
	"Configure ptppacket performance",
	"performance item",
	"Configure all items of ptppacket",'''
    for requestPerNameTemp in requestPerNameList:
        outString +='''
	"''' + requestPerNameTemp + '''",  //TODO:实现注释'''

    outString += '''
};

//////////////////////////////////

struct utons_cli_element set_performance_monitor_cli =
{
		"(索引 <1-255> type ''' + requestPerTabelName.lower() + '''	 item (all'''
    for requestPerNameTemp in requestPerNameList:
        outString +='|' + requestPerNameTemp.lower()

    outString +='''))| "   //TODO:实现索引
};

///////////////////////////////
int no_performance_monitor (struct utons_cli *cli, int argc, char **argv)
{
	int 索引 = 0; //TODO:实现索引
	
	//.............
	
	else if(0 == strcmp(argv[0], "索引")) //TODO:实现索引
	{
		portindex = atoi(argv[1]);

		if(0 == strcmp(argv[3], "''' + requestPerTabelName.lower() + '''"))
		{
			pertype = PerObjTypeList_''' + requestPerTabelName.lower() + ''';

			if (0 == strcmp(argv[5], "''' + requestPerNameList[0].lower() + '''"))
			{
			    perId = (Short)(IdNameNode::QueryId(argv[5],perIdNameList));
			}'''
    for requestPerNameTemp in requestPerNameList[1:]:
        outString +='''
			else if (0 == strcmp(argv[5], "''' + requestPerNameTemp.lower() + '''"))
			{
			    perId = (Short)(IdNameNode::QueryId(argv[5],perIdNameList));
			}'''

    outString += '''
		}

		sprintf(fid, "\\\\\\\\\\\\索引=%d", 索引);    //TODO:实现索引
		sprintf(expression,"Fid='%s' AND PerId= %d AND PerType = %d", (const char*)fid, perId, pertype);
	}
}

///////////////////////

char *no_performance_monitor_help[] =
{
"索引",   //TODO:实现索引
"索引值",  //TODO:实现索引值
"Object type",
"Configure ''' + requestPerTabelName.lower() + ''' performance",
"performance item",
"Configure all items of ptppacket",'''
    for requestPerNameTemp in requestPerNameList:
        outString += '''
"''' + requestPerNameTemp + '''的注释",   //TODO:实现注释'''

    outString += '''
};

//////////////////////////////////

struct utons_cli_element no_performance_monitor_cli =
{
		"(索引 <索引范围> type ''' + requestPerTabelName.lower() + '''	 item (all'''

    for requestPerNameTemp in requestPerNameList:
        outString += '|' + requestPerNameTemp.lower()

    outString += '''))| "
};

////////////////////////////////

int clear_counters (struct utons_cli *cli, int argc, char **argv)
{
		else if(0 == strcmp(argv[i], "''' + requestPerTabelName.lower() + '''"))
		{
			rcd.AddNew();
			if(0 == strcmp(argv[0], "all"))
			{
				rcd.SetExtFid("\\\\");
				sprintf(mtncmd,"clrcurper:''' + requestPerTabelName.lower() + '''");
			}
			else if(0 == strcmp(argv[0], "15mins"))
			{
				sprintf(Fid,"\\\\\\\\\\\\索引=%s",argv[2]);   //TODO:实现索引
				rcd.SetExtFid(Fid);
				sprintf(mtncmd,"clrcurper:min15:''' + requestPerTabelName.lower() + '''"); 
		
			}
			else if(0 == strcmp(argv[0], "24hrs"))
			{
				sprintf(Fid,"\\\\\\\\\\\\索引=%s",argv[2]);   //TODO:实现索引
				rcd.SetExtFid(Fid);
				sprintf(mtncmd,"clrcurper:hour24:''' + requestPerTabelName.lower() + '''");
			}
			else if(0 == strcmp(argv[0], "random"))
			{
				sprintf(Fid,"\\\\\\\\\\\\索引=%s",argv[2]);   //TODO:实现索引
				rcd.SetExtFid(Fid);
				sprintf(mtncmd,"clrcurper:randomPeriod:''' + requestPerTabelName.lower() + '''");
			}

			rcd.SetCommand(mtncmd);

			cli_ret = dbMtnCmd.Add(rcd);
		}
	}
}

////////////////////////////////

char *clear_counters_help[] =
{
	"''' + requestPerTabelName.lower() + ''' performance",
	
	//...........
	
	"索引",									 //''' + requestPerTabelName.lower() + '''  //TODO:实现索引
	"索引值",      //实现索引值
	"Object type",
	"''' + requestPerTabelName.lower() + ''' performance",
	"performance item",
	"Configure all items of ''' + requestPerTabelName.lower() + '''",'''

    for requestPerNameTemp in requestPerNameList:
        outString +='''
	"''' + requestPerNameTemp + '''的注释",   //TODO:实现注释'''

    outString += '''
	"15 minutes performance counters",
	"24 hours performance counters",
	"Random Period (1-15min) performance counters",
}

/////////////////////////

struct utons_cli_element clear_counters_cli =
{
	"(all (.......|''' + requestPerTabelName.lower() + ''')) |"
	
	//..........
	
	"( (15mins | 24hrs | random) 索引 <索引范围>				type ''' + requestPerTabelName.lower() + '''	item (all'''

    for requestPerNameTemp in requestPerNameList:
        outString +=  '|' + requestPerNameTemp.lower()

    outString += '''))| "   //TODO:实现索引
}

///////////////////////////

INT BuildExpression(struct utons_cli *cli, char **argv, char expression[256])
{
	else if(0 == strcmp(argv[0], "索引")) //TODO:实现索引
	{
		sprintf(expression, "Fid='\\\\\\\\\\\\索引=%d' AND Type = %d", atoi(argv[1]), IdNameNode::QueryId(argv[3], perTypeList));   //TODO:实现索引
	}
}

//////////////////////////////////
void TranslateFid(const PerObjTypeList type, const String strFid, char result[], const SIZE_t size)
{
	switch (type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		{
			sscanf(strFid,"\\\\\\\\\\\\索引=%d",&itmp);   //TODO:实现索引
			NSPSNPrintf(result, size, "\\n索引: %d", itmp);   //TODO:实现索引
			break;
		}
	}
}

/////////////////////////


char *show_performance_monitor_help[] =
{
	"索引",   //TODO:实现索引
	"索引值",  //TODO:实现索引值
	"Object type",
	"Configure ''' + requestPerTabelName.lower() + ''' performance",
}

/////////////////////////////////////

struct utons_cli_element show_performance_monitor_cli =
{
	  "(索引 <索引范围> type ''' + requestPerTabelName.lower() + ''') | " //TODO:实现索引
}'''

    return outString



def getCliApiAlarmperH(requestPerTabelName, requestPerNameList):
    outString = '''
struct per_''' + requestPerTabelName.lower() + '''_cur
{

	String   Fid;			
'''
    for requestPerNameTemp in requestPerNameList:
        outString += '''
	Long64 ''' + requestPerNameTemp + ''';'''

    outString += '''

	per_''' + requestPerTabelName.lower() + '''_cur()
	{

		Fid=NULL;'''
    for requestPerNameTemp in requestPerNameList:
        outString += '''
		''' + requestPerNameTemp + ''' = 0;'''

    outString += '''
	}

	~per_''' + requestPerTabelName.lower() + '''_cur()
	{
		if (Fid)
		{
			NOICore::StringFree(Fid);
			Fid = NULL;
		}

	}	

	char* FormatInfo();	
};



INT per_counters_get(SEQUENCE<per_''' + requestPerTabelName.lower() + '''_cur>& per_''' + requestPerTabelName.lower() + '''_list, String expression=NULL);




struct per_''' + requestPerTabelName.lower() + '''_his
{

	String Fid;
	Long   Period;
	Long IdxNum;
	DateAndTime endTime;
'''

    for requestPerNameTemp in requestPerNameList:
        if not(re.search(r'Rate$', requestPerNameTemp)):
            outString += '''
	Long64 ''' + requestPerNameTemp + ''';'''

    outString += '''
		
	Octet slot;
	Boolean IsNa;
	Boolean IsDefect;
	
	per_''' + requestPerTabelName.lower() + '''_his()
	{
		Fid=NULL;		
		Period = 0;	
		IdxNum = 0;
		memset((void *)&endTime, 0, sizeof(DateAndTime));
'''
    for requestPerNameTemp in requestPerNameList:
        if not(re.search(r'Rate$', requestPerNameTemp)):
            outString += '''
		''' + requestPerNameTemp + ''' = 0;'''

    outString += '''

		slot = 0;
		IsNa = false;
		IsDefect = false;	
	}

	~per_''' + requestPerTabelName.lower() + '''_his()
	{
		if (Fid)
		{
			NOICore::StringFree(Fid);
			Fid = NULL;
		}

	}	

	char* FormatInfo();	
};



INT per_his_counters_get(SEQUENCE<per_''' + requestPerTabelName.lower() + '''_his>& per_''' + requestPerTabelName.lower() + '''_list, String expression=NULL);
'''

    return outString


def getCliApiAlarmperCPP(requestPerTabelName, requestPerNameList):
    outString ='''
#include "record_set_per''' + requestPerTabelName.lower() + '''cur.h"



#include "record_set_per''' + requestPerTabelName.lower() + '''his.h"





char* per_''' + requestPerTabelName.lower() + '''_cur::FormatInfo()
{
	char buffer[2000] = {0};

	MY_SNPRINTF(buffer, sizeof(buffer),"%sFid:				 %s\\n",  buffer,(const char*)Fid);'''

    for requestPerNameTemp in requestPerNameList:
        outString +='''
	MY_SNPRINTF(buffer, sizeof(buffer),"%s ''' + requestPerNameTemp + ''':      %Ld\\n", buffer, ''' + requestPerNameTemp + ''');'''

    outString += '''

	return NOICore::StringClone(TAG_CLI_AGENT, buffer);	
}


INT per_counters_get(SEQUENCE<per_''' + requestPerTabelName.lower() + '''_cur>& per_''' + requestPerTabelName.lower() + '''_list, String expression)
{
	CRecordSetPer''' + requestPerTabelName + '''Cur	recSet(TAG_CLI_AGENT);
	CDbSetPer''' + requestPerTabelName + '''Cur     	DbSet(TAG_CLI_AGENT, 0, 1);

	if (NULL != expression)
	{
		DbSet.Query("*", expression, recSet);
	}
	else
	{
		DbSet.Query("*", "", recSet);
	}

	int i = 0;

	Long IfIndex = 0;
	CBString DbStr;
	char buffer[500] ={0};
	int DbLen = recSet.GetRows();
	per_''' + requestPerTabelName.lower() + '''_list.Construct(TAG_CLI_AGENT);
	per_''' + requestPerTabelName.lower() + '''_list.ObjSetLength(DbLen);

	for (recSet.MoveFirst();
		i < DbLen; 
		i++, recSet.MoveNext())
	{'''
    for requestPerNameTemp in requestPerNameList:
        outString +='''
		recSet.Get''' + requestPerNameTemp + '''(per_''' + requestPerTabelName.lower() + '''_list[i].''' + requestPerNameTemp + ''');'''

    outString += '''
		recSet.GetFid(DbStr);
				
		sscanf((const char*)DbStr, "\\\\\\\\\\\\portindex=%d", &IfIndex);
		sprintf(buffer, "portindex=%d", IfIndex);


		per_''' + requestPerTabelName.lower() + '''_list[i].Fid = NOICore::StringClone(TAG_CLI_AGENT, buffer);	
	}

	return LRet_success;
};







char* per_''' + requestPerTabelName.lower() + '''_his::FormatInfo()
{
	char buffer[2000] = {0};
	
	MY_SNPRINTF(buffer, sizeof(buffer),"%s Fid:                  %s\\n",  buffer, (const char*)Fid); 
	MY_SNPRINTF(buffer, sizeof(buffer),"%s Index Number:         %d\\n", buffer, IdxNum);
	MY_SNPRINTF(buffer, sizeof(buffer),"%s End Time:             %04d-%02d-%02d,%02d:%02d:%02d\\n",  buffer, 
		endTime.wYear,endTime.byMonth,endTime.byDay,endTime.byHour,endTime.byMinute,endTime.bySecond);'''

    for requestPerNameTemp in requestPerNameList:
        if not(re.search(r'Rate$', requestPerNameTemp)):
            outString +='''
	MY_SNPRINTF(buffer, sizeof(buffer),"%s ''' + requestPerNameTemp + ''':      %Ld\\n", buffer, ''' + requestPerNameTemp + ''');'''

    outString += '''

	return NOICore::StringClone(TAG_CLI_AGENT, buffer);
}


INT per_his_counters_get(SEQUENCE<per_''' + requestPerTabelName.lower() + '''_his>& per_''' + requestPerTabelName.lower() + '''_list, String expression)
{
	CRecordSetPer''' + requestPerTabelName + '''His	recSet(TAG_CLI_AGENT);
	CDbSetPer''' + requestPerTabelName + '''His     	DbSet(TAG_CLI_AGENT, 0, 1);

	if (NULL != expression)
	{
		DbSet.Query("*", expression, recSet);
	}
	else
	{
		DbSet.Query("*", "", recSet);
	}

	int i = 0;

	Long IfIndex = 0;
	CBString DbStr;
	char buffer[500] ={0};
	int DbLen = recSet.GetRows();
	per_''' + requestPerTabelName.lower() + '''_list.Construct(TAG_CLI_AGENT);
	per_''' + requestPerTabelName.lower() + '''_list.ObjSetLength(DbLen);

	for (recSet.MoveFirst();
		i < DbLen;
		i++, recSet.MoveNext())
	{
		recSet.GetPeriod(per_''' + requestPerTabelName.lower() + '''_list[i].Period);
		recSet.GetIdxNum(per_''' + requestPerTabelName.lower() + '''_list[i].IdxNum);
		per_''' + requestPerTabelName.lower() + '''_list[i].IdxNum++;
		recSet.GetEndTime(per_''' + requestPerTabelName.lower() + '''_list[i].endTime);
'''
    for requestPerNameTemp in requestPerNameList:
        if not(re.search(r'Rate$', requestPerNameTemp)):
            outString += '''
		recSet.Get''' + requestPerNameTemp + '''(per_''' + requestPerTabelName.lower() + '''_list[i].''' + requestPerNameTemp + ''');'''

    outString += '''
		recSet.GetEndTime(per_''' + requestPerTabelName.lower() + '''_list[i].endTime);
		recSet.GetIdxNum(per_''' + requestPerTabelName.lower() + '''_list[i].IdxNum);
		recSet.GetSlot(per_''' + requestPerTabelName.lower() + '''_list[i].slot);
		recSet.GetIsDefect(per_''' + requestPerTabelName.lower() + '''_list[i].IsDefect);
		recSet.GetIsNa(per_''' + requestPerTabelName.lower() + '''_list[i].IsNa);
		
		recSet.GetFid(DbStr);

		sscanf((const char*)DbStr, "\\\\\\\\\\\\portindex=%d", &IfIndex);
		sprintf(buffer, "portindex=%d", IfIndex);

		per_ptppacket_list[i].Fid = NOICore::StringClone(TAG_CLI_AGENT, buffer);
	}

	return LRet_success;
};'''

    return outString


def getCMakeListsTxt(requestPerTabelName):
    return '''
IF(LINUX) ADD_DEFINITIONS(
    ADD_DEFINITIONS(
			-DPER_FB_''' + requestPerTabelName.upper() + '''
    )




IF(VXWORKS)
    ADD_DEFINITIONS(
			-DPER_FB_''' + requestPerTabelName.upper() + '''
    )




IF(MSVC) # FOR WIN32
    ADD_DEFINITIONS(
		-DPER_FB_''' + requestPerTabelName.upper() + '''
   )
    '''


def getPerNeModH(requestPerTabelName):
    return'''
class CPerNe : public INSPModule
{
public:
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	CDSSrc_PerNeMsgSrc* m_per''' + requestPerTabelName + '''HisTblHandle;
#endif
}'''


def getPerNeModCpp(requestPerTabelName, requestPerNameList):
    outString =  '''
CPerNe::CPerNe(const NSPMag::MODULEHANDLE hm, void* pCfg)
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	m_per''' + requestPerTabelName + '''HisTblHandle	= NULL;
#endif
}


CPerNe::~CPerNe()
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	if(m_per''' + requestPerTabelName + '''HisTblHandle)
	{
		m_per''' + requestPerTabelName + '''HisTblHandle->~CDSSrc_PerNeMsgSrc();
		NSPFree(m_per''' + requestPerTabelName + '''HisTblHandle);
		m_per''' + requestPerTabelName + '''HisTblHandle = NULL;
	}
#endif
}



INT CPerNe::InitModule(NSPMag* pMag,void* pCfg)
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	m_per''' + requestPerTabelName + '''HisTblHandle = NSPNEW(TAG_CMM_PER) CDSSrc_PerNeMsgSrc();
	if(m_per''' + requestPerTabelName + '''HisTblHandle)
	{
		m_per''' + requestPerTabelName + '''HisTblHandle->Init(m_hSch, m_ulFullModId, 
			TID_TO_TEID2(LDataType_Per''' + requestPerTabelName + '''His, te_spectable), this);
	}
	else
	{
		return LRet_failure;
	}
#endif
}



INT CPerNe::Start()
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	register_proxy_tbl_noexpression_hook(CRecordSetPer''' + requestPerTabelName + '''Cur::GetTableName(), TID_TO_TEID2(LDataType_Per''' + requestPerTabelName + '''Cur, te_spectable), PROXY_TBL_QUERY_TIMEOUT);
#endif
}



INT CPerNe::RegDsSrc()
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	m_per''' + requestPerTabelName + '''HisTblHandle->Start();
#endif
}


INT CPerNe::UnRegDsSrc()
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	m_per''' + requestPerTabelName + '''HisTblHandle->Stop();
#endif
}



INT CPerNe::SaveHistoryToFile(my_FILEP fp, SPerHisStorage* pNode, const Octet period, Long index, CBString &dataFidBuf)
{
	MPer''' + requestPerTabelName + '''* pData''' + requestPerTabelName + ''' = NULL;
	
	switch (pNode->type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		pData''' + requestPerTabelName + ''' = (MPer''' + requestPerTabelName + '''*)pHis->data.ParamOut();'''

    for requestPerNameTemp in requestPerNameList:
        outString += '''
		EXPORT_DATA_NEW(pData''' + requestPerTabelName + ''', ''' + requestPerNameTemp + ''', llTemp, period, pNode);'''

    outString += '''
		break;
	}
}



void CPerNe::ProcPerHisTable(SEQUENCE<MPerHistory>& data, const SEQUENCE<Long> & flag)
{
	//ptppacket
	else if (PerObjTypeList_''' + requestPerTabelName.lower() + '''== data[i].type)
	{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
		sData.dataType = TID_TO_TEID2(LDataType_Per''' + requestPerTabelName + '''His, te_spectable);
		WritePerHisTable((CRecordSetPer''' + requestPerTabelName + '''His*)p1, (MPer''' + requestPerTabelName + '''*)p2, (SPerPrim''' + requestPerTabelName + '''*)p3, sData, data, flag);
#endif	
	}
}




void CPerNe::ClearHistroicalPerTalbe()
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	ForceFullSync(TID_TO_TEID2(LDataType_Per''' + requestPerTabelName + '''His, te_spectable), m_ulFullModId, 0);
#endif
}'''
    return outString

def getPerChssModH(requestPerTabelName, requestPerTabelId):
    return '''
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
typedef CPerNode<SPerPrim''' + requestPerTabelName + ''', SPerPrim''' + requestPerTabelName + ''', SPerHis''' + requestPerTabelName + '''> CPerNode''' + requestPerTabelName.upper() + ''';
typedef CPerProcessBase<CPerNode''' + requestPerTabelName.upper() + ''', SPerPrim''' + requestPerTabelName + '''> CPerProcess''' + requestPerTabelName.upper() + ''';
#endif



class CPerChss : public CCardCmmUnit
{
protected:
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	CPerProcess''' + requestPerTabelName.upper() + '''* m_pPer''' + requestPerTabelName.upper() + ''';
#endif
};'''


def getPerChssModCpp(requestPerTabelName, requestPerTabelId):
    return '''
char* g_PerFbName[] = 
{
	"LPerFb_''' + requestPerTabelName.lower() + ''' = ''' + requestPerTabelId + '''",
	"LPerFb_max = ''' + str(int(requestPerTabelId)+1) + '''"       //TODO:修改最大值
};


CPerChss::CPerChss(NSPMag::MODULEHANDLE hModule, int ChssPos, void *pCfg, Boolean ifSupportCfp,NSPScheduleImp::SCHHANDLE hSchDsMsg)
:CCardCmmUnit(hModule, 
				 0,
				 0,
				 0,
				 0,
				 false,
				 "CPerChss")
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	PER_PROC_SET_NULL(''' + requestPerTabelName.upper() + ''');
#endif
}


CPerChss::~CPerChss()
{
	//根据配置生成process对象
	for (ULong i = 0; i < m_fbSupport.num; i++)
	{
		switch (m_fbSupport.fb[i])
		{
		case LPerFb_''' + requestPerTabelName.lower() + ''':
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
			PER_PROC_DELETE(''' + requestPerTabelName.upper() + ''');
#endif
			break;
		}
	}
}


INT CPerChss::Init(NSPTag hMem, NSPScheduleImp::SCHHANDLE hSch)
{
	//根据配置生成process对象
	for (ULong i = 0; i < m_fbSupport.num; i++)
	{
		switch (m_fbSupport.fb[i])
		{
		case LPerFb_''' + requestPerTabelName.lower() + ''':
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
			PER_PROC_CREATE(''' + requestPerTabelName.upper() + ''', LPerFb_''' + requestPerTabelName.lower() + ''');
#endif
			break;
		}
	}
}


LDataType PerSupport[] = 
{
	LDataType_Per''' + requestPerTabelName + '''Cur
};



INT CPerChss::Cur2His(time_t StartTime, time_t EndTime, const Octet periodType)
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	PER_PROC_CUR2HIS(periodType, StartTime, EndTime, ''' + requestPerTabelName.upper() + ''');
#endif
}



INT CPerChss::ClearCurPer(Long64 fid, Long type, const Octet period, String expression, Short perId)
{
	switch (type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
		PER_PROC_CLR_CUR_DATA(''' + requestPerTabelName.upper() + ''', fid, period, perId);
#endif
		break;
	}
}


void CPerChss::ClearCurPerAlarm(Long64 fid, Long type, const Octet period)
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	PER_PROC_CLEAR_ALM(''' + requestPerTabelName.upper() + ''');
#endif
}


INT CPerChss::GetPrimData()
{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
		PER_PROC_GET_PRIM(''' + requestPerTabelName.upper() + ''');   //TODO:根据是否是5秒周期决定是否放到if (0 == m_count%5)中
#endif
}


INT CPerChss::QueryCurPer(VTable& vTable, Long type, String expression)
{
	else if (TID_TO_TEID2(LDataType_PerPtpPacketCur, te_spectable)== type)
	{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
		if (m_pPer''' + requestPerTabelName.upper() + ''')
		{
			CRecordSetPer''' + requestPerTabelName + '''Cur rec(TAG_CMM_PER);
			ret = m_pPer''' + requestPerTabelName.upper() + '''->AddToCurTable(&rec, expression);
			CopyVTable(vTable, *(rec.GetVTable()));
		}
#endif
	}
}



void CPerChss::dbgOutput()
{
	for (i = 0; i < m_fbSupport.num; i++)
	{
		else if (LPerFb_''' + requestPerTabelName.lower() + ''' == m_fbSupport.fb[i])
		{
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
			if (m_pPer''' + requestPerTabelName.upper() + ''')
			{
				m_pPer''' + requestPerTabelName.upper() + '''->selfInfo(buf);
			}
#endif	
		}
	}
}'''


def getPerChssHelperCpp(requestPerTabelName):
    return '''
void  CPerMonCfg_Helper_chss::Dispatch(void *pArg, TDSData * data)
{
	for (ULong i = 0; i < m_IncChg.Length(); i++)
	{
		switch (m_IncChg[i].type)
		{
		case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
			if (o.m_pPer''' + requestPerTabelName.upper() + ''')
				o.m_pPer''' + requestPerTabelName.upper() + '''->ProcNode(m_IncChg[i], ifRptHisData);
#endif
			break;
		}
	}
}


void  CPerMonItemCfg_Helper_chss::Dispatch(void *pArg, TDSData * data)
{
	for (ULong i = 0; i < m_IncChg.Length(); i++)
	{
		switch (m_IncChg[i].perType)
		{
		case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
			if (o.m_pPer''' + requestPerTabelName.upper() + ''')
				o.m_pPer''' + requestPerTabelName.upper() + '''->ProcNode(m_IncChg[i], ifRptHisData);
#endif
			break;
		}
	}
}'''


def getNeSvcCfgLgCfgMngCpp(requestPerTabelName):
    return '''
void CNeSvcLgCardMng::sJobPerMonitorCheck(void* p1, void*p2)
{
	for (i=0,recPerMonitor.MoveFirst(); i<recPerMonitor.GetRows(); i++,recPerMonitor.MoveNext())
	{
		else if (Type == PerObjTypeList_''' + requestPerTabelName.lower() + ''')
		{
		    //TODO:以下两行改成根据实际FID获取Express
			sscanf((const char*)Fid, "\\\\\\interface=%d", &IfIndex);
			sprintf(Express, "IfIndex='\\\\\\interface=%d'", IfIndex);

			if(CNeSvcDbTool::GetRecordRows(CRecordSet''' + requestPerTabelName + '''DSCfg::GetTableName(), Express, LDcDataView_config) > 0)    //TODO：需要将"CRecordSet''' + requestPerTabelName + '''DSCfg"修改成实际对应的表
				continue;
		}
	}
}'''

def getNeSvcCommDataMtnCpp(requestPerTabelName):
    return'''
INT CNeSvcDataType_PerMonitorCfg::Format_DataType(void* pTMsg, INT DT_POS, String FormatString)
{
	switch (p->type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		strcat(TypeStr, " PerObjTypeList_''' + requestPerTabelName.lower() + '''");
		break;
	}
}


INT CNeSvcDataType_PerMonitorItemCfg::Format_DataType(void* pTMsg, INT DT_POS, String FormatString)
{
	switch (p->perType)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		strcat(TypeStr, " PerObjTypeList_''' + requestPerTabelName.lower() + '''");
		break;
	}
}'''

def getNeSvcCommDataDecomposeCpp(requestPerTabelName):
    return '''
INT CNeSvcCommData::GetSlotForSiglePerObj(Long SessionId, TMsgPerMonitorCfg cfg, Long& slot)
{
	switch (cfg.type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
	{
		//TODO:获取槽位号
		slot = 获取到的槽位号，从1开始;
		break;
	}
	}
}'''

def getNESvcCfgPerMonitorCfgCpp(requestPerTabelName):
    outString = '''
int Check(Long index, Long type, bool& support)
{
		if (type == PerObjTypeList_''' + requestPerTabelName.lower() + ''')
		{
			support = true;
		}
}'''
    outString += '''



INT CNeSvcCfg::TPerMonitorCfgOpHookBefore(const MDCOpData * data, void * p1, void * p2, void * p3)
{
	else if (PerObjTypeList_''' + requestPerTabelName.lower() + ''' == type)
	{
		//TODO:以下两行改成根据实际FID获取Express
		sscanf((const char*)FidStr, "\\\\\\interface=%d", &index);
		sprintf(Exp, "IfIndex='\\\\\\interface=%d'", index);

		if(0 == CNeSvcDbTool::GetRecordRows(CRecordSet''' + requestPerTabelName + '''DSCfg::GetTableName(), Exp, LDcDataView_config))    //TODO：需要将"CRecordSet''' + requestPerTabelName + '''DSCfg"修改成实际对应的表
		{
			return LRet_objectNotExisted;
		}
	}
}'''

    outString += '''



INT CNeSvcCfg::TPerMonitorCfgTryHook(const MDCOpData * data, void * p1, void * p2, void * p3)
{
			else if (PerObjTypeList_''' + requestPerTabelName.lower() + ''' == type)
			{
				//TODO:以下两行改成根据实际FID获取Express
				sscanf((const char*)FidStr, "\\\\\\interface=%d", &index);
				sprintf(Exp, "IfIndex='\\\\\\interface=%d'", index);

				if(0 == CNeSvcDbTool::GetRecordRows(CRecordSet''' + requestPerTabelName + '''DSCfg::GetTableName(), Exp, LDcDataView_config))    //TODO：需要将"CRecordSet''' + requestPerTabelName + '''DSCfg"修改成实际对应的表
				{
					return LRet_objectNotExisted;
				}
			}
}'''

    return outString


def getMtnCmdDcCpp(requestPerTabelName):
    return '''
INT CMtnCmdDc::OpHook_After_MtnCmd_Add(void* pArg1, void* pArg2, const CBString& TblName, const SEQUENCE<TColValue>& listData, const CBString& expression)
{
	for (ULong i=0; i<cnt; i++, rcd.MoveNext())
	{
		if (NULL != strstr(CBStr2Str(command), "clrcurper"))
		{
			do {
					else if(0 == strcmp(para,"''' + requestPerTabelName.lower() + '''"))
					{
                        seqPerCmd[0].type = PerObjTypeList_''' + requestPerTabelName.lower() + ''';
					}
			}while (NULL != sp);
		}
	}
}'''

def getToolFidCpp(requestPerTabelName):
    return '''
extern INT CvtFid2StrToLong64( const String sFid, const PerObjTypeList type, Long64& llFid )
{
	switch (type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		if (0 == strcmp(info[0].name, "FID索引"))     //TODO：填上"FID索引"
		{
			uFid.''' + requestPerTabelName.lower() + '''Fid.FID索引 = (Octet)(info[i].value); //TODO：填上"FID索引"，可能需要修改上一层"''' + requestPerTabelName.lower() + '''Fid"
		}
		break;
	}
}''' + '''


extern INT CvtFid2Long64ToStr(const Long64 llFid, const PerObjTypeList type, String sFid , ULong len_sFid)
{
	switch (type)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':
		NSPSNPrintf(sFid, len_sFid, "\\\\\\FID索引=%d", fid->fid.value);       //TODO：填上"FID索引"
		break;
	}
}'''

def getPerToolsCpp(requestPerTabelName, requestPerTabelId, requestPerNameList):
    outString = '''
const Short perIdList[][MAX_PRIM_COUNT] = 
{
	{'''

    for requestPerNameTemp in requestPerNameList:
        outString += '''
		LPerId_''' + requestPerNameTemp + ''','''

    outString += '''
		LPerId_DefaultID
	},  //''' + requestPerTabelName.lower() + '''     PerObjTypeList_''' + requestPerTabelName.lower() + ''' = ''' + requestPerTabelId + '''
};



'''
    outString +='''
const PER_FB_INFO_ITEM perFbInfoTable[LPerFb_max] = 
{
	{
		LPerId_''' + requestPerNameList[0] + ''', ''' + str(len(requestPerNameList)) + ''', 0,
 		{0, 0, 0, 0, 0, 0, 0, 0},   //TODO:填上本地检测的告警列表
 		{0, 0, 0, 0, 0, 0, 0, 0},   //TODO:填上远端缺陷的告警列表
	},  //''' + requestPerTabelName.lower() + '''     LPerFb_''' + requestPerTabelName.lower() + ''' = ''' + requestPerTabelId + '''
};



'''
    outString += '''
INT PerUtility::PerObjType2FidType( const PerObjTypeList objType, LFidType& fidType )
{
	switch (objType)
	{
	case PerObjTypeList_''' + requestPerTabelName.lower() + ''':	
		fidType = LFidType_''' + requestPerTabelName.lower() + ''';
		break;
	}
}



'''
    outString += '''
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
/***********************************************************/
/* ''' + requestPerTabelName + ''' performance性能                               */
/***********************************************************/

SPerPrim''' + requestPerTabelName + '''::SPerPrim''' + requestPerTabelName + '''()
{
	Init();
}

void SPerPrim''' + requestPerTabelName + '''::Init()
{
	memset(this, 0, sizeof(SPerPrim''' + requestPerTabelName + '''));
}

void SPerPrim''' + requestPerTabelName + '''::InitItem(Short perId)
{
	switch(perId)
	{'''

    for requestPerNameTemp in requestPerNameList:
        outString += '''
	case LPerId_''' + requestPerNameTemp + ''':
		''' + requestPerNameTemp + ''' = 0;
		break;'''

    outString += '''
	default:
		break;
	}
}

void SPerPrim''' + requestPerTabelName + '''::Calc( SPerPrim''' + requestPerTabelName + '''& prim, Long* alm, Long& Cur, char* Cnt, Long& CurExt, char* CntExt, Long& feCur, char* feCnt, Long vel )
{
	NSP_TEMP_UNUSED_ARG(CurExt);
	NSP_TEMP_UNUSED_ARG(CntExt);
	NSP_TEMP_UNUSED_ARG(feCnt);
	NSP_TEMP_UNUSED_ARG(feCur);
	NSP_TEMP_UNUSED_ARG(Cnt);
	NSP_TEMP_UNUSED_ARG(Cur);
	NSP_TEMP_UNUSED_ARG(alm);
	NSP_TEMP_UNUSED_ARG(vel);
}

void SPerPrim''' + requestPerTabelName + '''::Update( SPerPrim''' + requestPerTabelName + '''& newData )
{'''

    hasRate = False
    for requestPerNameTemp in requestPerNameList:
        if (re.search(r'Rate$', requestPerNameTemp)):
            hasRate = True
            addStringTemp = '''
	PER_PRIM_GET_RATE_NEW(''' + re.sub(r'Rate$', '', requestPerNameTemp) + ''', time_count_five ); //TODO: 根据更新周期不同修改time_count_five
	setRate(''' + requestPerNameTemp + '''Array, 10, ''' + requestPerNameTemp + ''', m_cur);
            '''
        else:
            addStringTemp = '''
	PER_PRIM_ADD_NEW(''' + requestPerNameTemp + ''');'''
        outString += addStringTemp

    if(hasRate):
        outString += '''
	m_cur = (++m_cur)%10;'''

    outString += '''
}

void SPerPrim''' + requestPerTabelName + '''::Cur2His( SPerPrimPtpPacket* pRec, const Octet period )
{'''
    for requestPerNameTemp in requestPerNameList:
        if not(re.search(r'Rate$', requestPerNameTemp)):
            outString += '''
	PER_PRIM_CUR2HIS_DEFECT64_NEW(pRec, ''' + requestPerNameTemp + ''');'''

    outString +='''
}

void SPerPrim''' + requestPerTabelName + '''::SetPerItmMonCfg(Short perId,Boolean MonStat)
{
	switch(perId)
	{'''

    for requestPerNameTemp in requestPerNameList:
        outString +='''
	case LPerId_''' + requestPerNameTemp + ''':
		''' + requestPerNameTemp + '''MonStat = MonStat;
		break;'''

    outString +='''
	default:
		break;
	}
}

void SPerPrim''' + requestPerTabelName + '''::AddToRecordSet( const String sFid, const Octet period, void* pRec)
{
	NSP_TEMP_UNUSED_ARG(period);
	NSP_TEMP_UNUSED_ARG(pRec);
	NSP_TEMP_UNUSED_ARG(sFid);
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	CRecordSetPerPtpPacketCur* pRow = (CRecordSetPerPtpPacketCur*)pRec;
	pRow->AddNew();
	if (sFid)
	{
		pRow->SetFid(sFid);
	}
	pRow->SetRowStatus(LRowStaus_add);'''

    hasRate = False
    addRateStringTemp = ''
    for requestPerNameTemp in requestPerNameList:
        if (re.search(r'Rate$', requestPerNameTemp)):
            hasRate = True
            addRateStringTemp += '''
		''' + requestPerNameTemp + ''' = getRate(''' + requestPerNameTemp + '''Array, 10);
		PER_PRIM_SET_REC_NEW(pRow, ''' + requestPerNameTemp + ''');'''
        else:
            outString +='''
	PER_PRIM_SET_REC_NEW(pRow, ''' + requestPerNameTemp + ''');'''

    if (hasRate):
        outString += '''

	if (PerPeriodList_Min15 == period)
	{
        ''' + addRateStringTemp + '''
	}'''

    outString += '''

	pRow->Setperiod(period);
#endif
}

void SPerPrim''' + requestPerTabelName + '''::SetHisRec( void* pRec )
{
	NSP_TEMP_UNUSED_ARG(pRec);
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
	CRecordSetPer''' + requestPerTabelName + '''His* pRow = (CRecordSetPer''' + requestPerTabelName + '''His*)pRec;
    '''

    for requestPerNameTemp in requestPerNameList:
        if not (re.search(r'Rate$', requestPerNameTemp)):
            outString +='''
	PER_PRIM_SET_REC(pRow, ''' + requestPerNameTemp + ''');'''

    outString += '''

#endif
}

void SPerPrim''' + requestPerTabelName + '''::CreateAnyData( Any& data )
{
	MPer''' + requestPerTabelName + ''' per;
    '''

    for requestPerNameTemp in requestPerNameList:
        if not (re.search(r'Rate$', requestPerNameTemp)):
            outString += '''
	PER_VALUE_SET(per, ''' + requestPerNameTemp + ''');'''

    outString += '''
	data.Insert(TID_TO_TEID(TID_MPer''' + requestPerTabelName + '''), &per, TAG_CMM_PER);
}

void SPerPrim''' + requestPerTabelName + '''::JudgeCrossThr( const Octet period, Long64 fid, MPerThr* thr, SEQUENCE<MAlmChss>& alm )
{
	NSP_TEMP_UNUSED_ARG(period);
	NSP_TEMP_UNUSED_ARG(fid);
	NSP_TEMP_UNUSED_ARG(thr);
	NSP_TEMP_UNUSED_ARG(alm);
}

void SPerPrim''' + requestPerTabelName + '''::ClearCrossThrAlm( const Octet period, Long64 fid, SEQUENCE<MAlmChss>& alm )
{
	NSP_TEMP_UNUSED_ARG(period);
	NSP_TEMP_UNUSED_ARG(fid);
	NSP_TEMP_UNUSED_ARG(alm);
}

void SPerPrim''' + requestPerTabelName + '''::ClearSingleCrossThrAlm(const Octet period, Long64 fid, Short perid, SEQUENCE<MAlmChss>& alm)
{
	NSP_TEMP_UNUSED_ARG(period);
	NSP_TEMP_UNUSED_ARG(fid);
	NSP_TEMP_UNUSED_ARG(perid);
	NSP_TEMP_UNUSED_ARG(alm);
}
void SPerPrim''' + requestPerTabelName + '''::MakeInfo( String dataBuf, Long len )
{
	if (NULL == dataBuf)
	{
		return;
	}

	memset(dataBuf, 0, len);
    '''

    for requestPerNameTemp in requestPerNameList:
        if not (re.search(r'Rate$', requestPerNameTemp)):
            outString += '''
	PER_PRIM_INFO(''' + requestPerNameTemp + ''');'''

    outString += '''
}
#endif'''

    return outString


def getPerToolsH(requestPerTabelName, requestPerNameList):
    outString = '''
#ifdef PER_FB_''' + requestPerTabelName.upper() + '''
#include "record_set_per''' + requestPerTabelName.lower() + '''cur.h"
#include "record_set_per''' + requestPerTabelName.lower() + '''his.h"
#endif


#ifdef PER_FB_''' + requestPerTabelName.upper() + '''

/////////////////////////////////////////////////////////////////////////
//	''' + requestPerTabelName + ''' performance data define 
/////////////////////////////////////////////////////////////////////////

struct SPerPrim''' + requestPerTabelName + '''
{'''

    addStringTemp = ''
    hasRate = False
    for requestPerNameTemp in requestPerNameList:
        outString += '''
	Long64 ''' + requestPerNameTemp + ''';'''
        if (re.search(r'Rate$', requestPerNameTemp)):
            hasRate = True
            addStringTemp += '''
	Long64 ''' + requestPerNameTemp + '''Array[10];'''

    if (hasRate):
        outString += '''

	int m_cur;
'''
        outString += addStringTemp

    for requestPerNameTemp in requestPerNameList:
        outString += '''
	Boolean ''' + requestPerNameTemp + '''MonStat;'''

    outString +='''

    SPerPrim''' + requestPerTabelName + '''();


	void Init();

	void InitItem(Short perId);

	void Calc( SPerPrim''' + requestPerTabelName + '''& prim, Long* alm, Long& Cur, char* Cnt, Long& CurExt, char* CntExt, Long& feCur, char* feCnt, Long vel );

	void Update(SPerPrim''' + requestPerTabelName + '''& newData);

	void Cur2His(SPerPrim''' + requestPerTabelName + '''* pRec, const Octet period);

	void AddToRecordSet( const String sFid, const Octet period, void* pRec);

	void SetHisRec(void* pRec);

	void CreateAnyData(Any& data);

	void JudgeCrossThr(const Octet period, Long64 fid, MPerThrCfg* thr, SEQUENCE<MAlmChss>& alm);

	void ClearCrossThrAlm(const Octet period, Long64 fid, SEQUENCE<MAlmChss>& alm);

	void ClearSingleCrossThrAlm(const Octet period, Long64 fid, Short perid, SEQUENCE<MAlmChss>& alm);

	void MakeInfo(String dataBuf, Long len);

	void SetPerItmMonCfg(Short perId,Boolean MonStat);
	
};


struct SPerHis''' + requestPerTabelName + '''
{
	Long idx;
	Boolean isNa;
	Boolean isDefect;
	time_t endTime;
	SPerPrim''' + requestPerTabelName + ''' per;
};
#endif
'''
    return outString

def getXXXWs():
    global PerXXXCur
    global PerXXXHis
    return '''
	<Spec>''' + PerXXXCur['name'] + '''.V0.ts</Spec>
	<Spec>''' + PerXXXHis['name'] + '''.V0.ts</Spec>
    '''


def getLPerFb(requestPerTabelName, requestPerTabelId):
    return '''
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="Short" val="''' + requestPerTabelId + '''"/>
            </Any>
            <Any>
              <val teid="String" val="中文注释"/>
            </Any>
            <Any>
              <val teid="String" val="中文注释"/>
            </Any>
            <Any>
              <val teid="String" val="''' + requestPerTabelName + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + requestPerTabelName + '''"/>
            </Any>
          </val>
        </val>
      </Any>
'''


def getLDataType():
    global PerXXXCur
    global PerXXXHis
    return '''
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="Short" val="cur的ID"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXCur['name'] + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXCur['name'] + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXCur['name'] + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXCur['name'] + '''"/>
            </Any>
          </val>
        </val>
      </Any>
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="Short" val="his的ID"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXHis['name'] + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXHis['name'] + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXHis['name'] + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + PerXXXHis['name'] + '''"/>
            </Any>
          </val>
        </val>
      </Any>
    '''


def getDataTypeDef():
    global PerXXXCur
    global PerXXXHis
    return '''
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="String" val="''' + PerXXXCur['name'] + '''"/>
            </Any>
            <Any>
              <val teid="Long" val="cur的ID"/>
            </Any>
            <Any>
              <val teid="Long" val="0"/>
            </Any>
          </val>
        </val>
      </Any>
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="String" val="''' + PerXXXHis['name'] + '''"/>
            </Any>
            <Any>
              <val teid="Long" val="his的ID"/>
            </Any>
            <Any>
              <val teid="Long" val="0"/>
            </Any>
          </val>
        </val>
      </Any>
    '''


def getPerObjTypeList(requestPerTabelName, requestPerTabelId):
    return '''
        <Any>
          <val teid="Any_Seq">
            <val>
              <Any>
                <val teid="Short" val="''' + requestPerTabelId + '''"/>
              </Any>
              <Any>
                <val teid="String" val="''' + requestPerTabelName.lower() + '''"/>
              </Any>
              <Any>
                <val teid="String" val="''' + requestPerTabelName.lower() + '''"/>
              </Any>
              <Any>
                <val teid="String" val="''' + requestPerTabelName.lower() + '''"/>
              </Any>
              <Any>
                <val teid="String" val="''' + requestPerTabelName.lower() + '''"/>
              </Any>
            </val>
          </val>
        </Any>
              '''


def getNeBaseOtrEnd(requestPerTabelName):
    return '''
</attrib>




<str value="MPer''' + requestPerTabelName + '''"></str>

            '''


def getNeBaseOtrData(requestPerNameTemp):
    return '''
<attribelem typename="Long64" typekind="0" typeid="0" acl="3" name="''' + requestPerNameTemp + '''">
<memo id="0"><![CDATA[]]></memo>
<memo id="1"><![CDATA[]]></memo>
<memo id="2"><![CDATA[]]></memo>
</attribelem>
            '''


def getNeBaseOtrStart(requestPerTabelName):
    neBase = '''
<attrib key="MPer''' + requestPerTabelName + '''">
<prop typekind="0" typeid="组ID" size="0" name="MPer''' + requestPerTabelName + '''">
</prop>
<parent value=""></parent>
<memo id="0"><![CDATA[]]></memo>
<memo id="1"><![CDATA[]]></memo>
<memo id="2"><![CDATA[]]></memo>
            '''
    return neBase


def setPerXXXHisEnd(PerXXXHis):
    PerXXXHis['data'] += '''
      <TableSpecField id="Slot" acl="0" type="Octet">
        <disp/>
        <memo/>
        <defaultVal teid="Octet" val="0"/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="Hidden">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
          <KVAnyPair key="IsKey">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
      <TableSpecField id="IsNa" acl="0" type="Boolean">
        <disp/>
        <memo/>
        <defaultVal teid="Boolean" val="true"/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="Hidden">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
      <TableSpecField id="IsDefect" acl="0" type="Boolean">
        <disp/>
        <memo/>
        <defaultVal teid="Boolean" val="false"/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="Hidden">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
    </field>
    <index/>
    <map/>
    <param/>
  </Spec>
</ObjectPersistSpace>
                '''


def setPerXXXHisStart(PerXXXHis, requestPerTabelName):
    PerXXXHis['name'] = 'Per' + requestPerTabelName + 'His'
    PerXXXHis['data'] = '''
<?xml version="1.0" encoding="UTF-8"?>

<ObjectPersistSpace>
  <Spec id="Per''' + requestPerTabelName + '''His.VX" acl="0" sh="per:Per''' + requestPerTabelName + '''His">
    <disp>
      <String val="英文注释"/>
      <String val="中文注释"/>
    </disp>
    <memo>
      <String val="英文缩写"/>
      <String val="英文缩写"/>
    </memo>
    <hook/>
    <limit/>
    <field>
      <TableSpecField id="Fid" acl="0" type="String">
        <disp>
          <String val="FID"/>
          <String val="FID"/>
        </disp>
        <memo>
          <String val="FID"/>
          <String val="FID"/>
        </memo>
        <defaultVal teid="String" val=""/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="IsKey">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
          <KVAnyPair key="Limit">
            <val teid="String" val="size:0..64"/>
          </KVAnyPair>
          <KVAnyPair key="IsFid">
            <val teid="Octet" val="2"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
      <TableSpecField id="Period" acl="0" type="Long">
        <disp>
          <String val="Performance Period"/>
          <String val="性能周期"/>
        </disp>
        <memo>
          <String val="Performance Period"/>
          <String val="性能周期"/>
        </memo>
        <defaultVal teid="Long" val="0"/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="IsKey">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
          <KVAnyPair key="Limit">
            <val teid="String" val="{PerPeriodList.V1}"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
      <TableSpecField id="IdxNum" acl="0" type="Long">
        <disp>
          <String val="Record ID"/>
          <String val="记录编号"/>
        </disp>
        <memo>
          <String val="Record ID"/>
          <String val="记录编号"/>
        </memo>
        <defaultVal teid="Long" val="0"/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="Limit">
            <val teid="String" val="[0,95]"/>
          </KVAnyPair>
          <KVAnyPair key="IsKey">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
      <TableSpecField id="EndTime" acl="0" type="DateAndTime">
        <disp>
          <String val="Period End Time"/>
          <String val="周期结束时间"/>
        </disp>
        <memo>
          <String val="Period End Time"/>
          <String val="周期结束时间"/>
        </memo>
        <defaultVal teid="DateAndTime" wYear="70" byMonth="11" byDay="31" byHour="0" byMinute="0" bySecond="0" byCentisecond="0"/>
        <flag/>
        <hook/>
        <param/>
      </TableSpecField>
        '''


def setPerXXXCurEnd(PerXXXCur):
    PerXXXCur['data'] += '''
      <TableSpecField id="period" acl="0" type="Octet">
        <disp>
          <String val="Performance Statistic Period Enum"/>
          <String val="性能统计周期枚举"/>
        </disp>
        <memo>
          <String val="Performance Statistic Period Enum"/>
          <String val="性能统计周期枚举"/>
        </memo>
        <defaultVal teid="Octet" val="0"/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="IsKey">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
          <KVAnyPair key="Limit">
            <val teid="String" val="{PerPeriodList.V1}"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
    </field>
    <index/>
    <map/>
    <param>
      <KVAnyPair key="IsProxy">
        <val teid="Boolean" val="true"/>
      </KVAnyPair>
    </param>
  </Spec>
</ObjectPersistSpace>
        '''


def setPerXXXCurStart(PerXXXCur, requestPerTabelName):
    PerXXXCur['name'] = 'Per' + requestPerTabelName + 'Cur'
    PerXXXCur['data'] = '''
<?xml version="1.0" encoding="UTF-8"?>

<ObjectPersistSpace>
  <Spec id="Per''' + requestPerTabelName + '''Cur.VX" acl="0" sh="per:per''' + requestPerTabelName + '''Cur">
    <disp>
      <String val="英文注释"/>
      <String val="中文注释"/>
    </disp>
    <memo>
      <String val="英文缩写"/>
      <String val="英文缩写"/>
    </memo>
    <hook/>
    <limit/>
    <field>
      <TableSpecField id="Fid" acl="0" type="String">
        <disp>
          <String val="FID"/>
          <String val="FID"/>
        </disp>
        <memo>
          <String val="Fid"/>
          <String val="Fid"/>
        </memo>
        <defaultVal teid="String" val=""/>
        <flag/>
        <hook/>
        <param>
          <KVAnyPair key="Limit">
            <val teid="String" val="size:0..64"/>
          </KVAnyPair>
          <KVAnyPair key="IsKey">
            <val teid="Boolean" val="true"/>
          </KVAnyPair>
          <KVAnyPair key="IsFid">
            <val teid="Octet" val="2"/>
          </KVAnyPair>
        </param>
      </TableSpecField>
        '''


def getPerXXXHisData(requestPerNameTemp):
    return '''
      <TableSpecField id="''' + requestPerNameTemp + '''" acl="0" type="Long64">
        <disp>
          <String val="英文注释"/>
          <String val="中文注释"/>
        </disp>
        <memo>
          <String val="英文注释"/>
          <String val="中文注释"/>
        </memo>
        <defaultVal teid="Long64" val="0"/>
        <flag/>
        <hook/>
        <param/>
      </TableSpecField>
            '''


def getPerXXXCurData(requestPerNameTemp):
    return '''
      <TableSpecField id="''' + requestPerNameTemp + '''" acl="0" type="Long64">
        <disp>
          <String val="英文注释"/>
          <String val="中文注释"/>
        </disp>
        <memo>
          <String val="英文注释"/>
          <String val="中文注释"/>
        </memo>
        <defaultVal teid="Long64" val="0"/>
        <flag/>
        <hook/>
        <param/>
      </TableSpecField>            
            '''


def getLPerPrimId(requestPerIdTemp, requestPerNameTemp):
    return '''
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="Short" val="''' + str(requestPerIdTemp) + '''"/>
            </Any>
            <Any>
              <val teid="String" val="''' + requestPerNameTemp + '''"/>
            </Any>
            <Any>
              <val teid="String" val=""/>
            </Any>
            <Any>
              <val teid="String" val="''' + requestPerNameTemp + '''"/>
            </Any>
            <Any>
              <val teid="String" val=""/>
            </Any>
          </val>
        </val>
      </Any>
            '''


def getPerIdUnit(requestPerIdTemp):
    return '''
      <Any>
        <val teid="Any_Seq">
          <val>
            <Any>
              <val teid="Short" val="''' + str(requestPerIdTemp) + '''"/>
            </Any>
            <Any>
              <val teid="String" val="英文单位"/>
            </Any>
            <Any>
              <val teid="String" val="中文单位"/>
            </Any>
            <Any>
              <val teid="String" val="中文单位"/>
            </Any>
            <Any>
              <val teid="String" val="英文单位"/>
            </Any>
            <Any>
              <val teid="String" val="英文单位"/>
            </Any>
          </val>
        </val>
      </Any>            
            '''


def getLPerId(requestPerIdTemp, requestPerNameTemp):
    LPerIdTemp = '''
        <Any>
          <val teid="Any_Seq">
            <val>
              <Any>
                <val teid="Short" val="''' + str(requestPerIdTemp) + '''"/>
              </Any>
              <Any>
                <val teid="String" val="中文注释"/>
              </Any>
              <Any>
                <val teid="String" val="中文注释"/>
              </Any>
              <Any>
                <val teid="String" val="''' + requestPerNameTemp + '''"/>
              </Any>
              <Any>
                <val teid="String" val="英文注释"/>
              </Any>
            </val>
          </val>
        </Any>
              '''
    return LPerIdTemp
