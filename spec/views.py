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


def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("hello world!")
    global requestPerTabelName, requestPerList, LPerId, PerIdUnit, LPerPrimId, PerXXXCur, PerXXXHis, neBase,\
        PerObjTypeList, DataTypeDef, LDataType, LPerFb, XXXWs, perToolsCpp
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

    return render(request, "index.html", {'tableName': requestPerTabelName, 'data': requestPerList, 'LperIdTd': LPerId,
                                          'PerIdUnitTd': PerIdUnit, 'LPerPrimIdTd': LPerPrimId,
                                          'PerXXXCurTd': PerXXXCur, 'PerXXXHisTd': PerXXXHis,
                                          'neBaseOtrXml': neBase, 'PerObjTypeList': PerObjTypeList,
                                          'DataTypeDef': DataTypeDef, 'LDataType': LDataType,
                                          'LPerFb': LPerFb, 'XXXWs': XXXWs, 'perToolsCpp': perToolsCpp})

def getPerToolsCpp(requestPerTabelName, requestPerTabelId, requestPerNameList):
    perToolsCppTemp = '''
const Short perIdList[][MAX_PRIM_COUNT] = 
{
	{'''

    for requestPerNameTemp in requestPerNameList:
        perToolsCppTemp += '''
		LPerId_''' + requestPerNameTemp + ''','''

    perToolsCppTemp += '''
		LPerId_DefaultID
	},  //''' + requestPerTabelName.lower() + '''     PerObjTypeList_''' + requestPerTabelName.lower() + ''' = ''' + requestPerTabelId + '''
};



'''
    perToolsCppTemp +='''
const PER_FB_INFO_ITEM perFbInfoTable[LPerFb_max] = 
{
	{
		LPerId_''' + requestPerNameList[0] + ''', ''' + str(len(requestPerNameList)) + ''', 0,
 		{0, 0, 0, 0, 0, 0, 0, 0},   //TODO:填上本地检测的告警列表
 		{0, 0, 0, 0, 0, 0, 0, 0},   //TODO:填上远端缺陷的告警列表
	},  //''' + requestPerTabelName.lower() + '''     PerObjTypeList_''' + requestPerTabelName.lower() + ''' = ''' + requestPerTabelId + '''
};



'''
    perToolsCppTemp += '''
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
    perToolsCppTemp += '''
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
        perToolsCppTemp += '''
	case LPerId_''' + requestPerNameTemp + ''':
		''' + requestPerNameTemp + ''' = 0;
		break;'''

    perToolsCppTemp += '''
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
        perToolsCppTemp += addStringTemp

    if(hasRate):
        perToolsCppTemp += '''
	m_cur = (++m_cur)%10;'''

    perToolsCppTemp += '''
}

void SPerPrim''' + requestPerTabelName + '''::Cur2His( SPerPrimPtpPacket* pRec, const Octet period )
{'''
    for requestPerNameTemp in requestPerNameList:
        if not(re.search(r'Rate$', requestPerNameTemp)):
            perToolsCppTemp += '''
	PER_PRIM_CUR2HIS_DEFECT64_NEW(pRec, ''' + requestPerNameTemp + ''');'''

    perToolsCppTemp +='''
}

void SPerPrim''' + requestPerTabelName + '''::SetPerItmMonCfg(Short perId,Boolean MonStat)
{
	switch(perId)
	{'''

    for requestPerNameTemp in requestPerNameList:
        perToolsCppTemp +='''
	case LPerId_''' + requestPerNameTemp + ''':
		''' + requestPerNameTemp + '''MonStat = MonStat;
		break;'''

    perToolsCppTemp +='''
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
            perToolsCppTemp +='''
	PER_PRIM_SET_REC_NEW(pRow, ''' + requestPerNameTemp + ''');'''

    if (hasRate):
        perToolsCppTemp += '''

	if (PerPeriodList_Min15 == period)
	{
        ''' + addRateStringTemp + '''
	}'''

    perToolsCppTemp += '''

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
            perToolsCppTemp +='''
	PER_PRIM_SET_REC(pRow, ''' + requestPerNameTemp + ''');'''

    perToolsCppTemp += '''

#endif
}

void SPerPrim''' + requestPerTabelName + '''::CreateAnyData( Any& data )
{
	MPer''' + requestPerTabelName + ''' per;
    '''

    for requestPerNameTemp in requestPerNameList:
        if not (re.search(r'Rate$', requestPerNameTemp)):
            perToolsCppTemp += '''
	PER_VALUE_SET(per, ''' + requestPerNameTemp + ''');'''

    perToolsCppTemp += '''
	data.Insert(TID_TO_TEID(TID_MPer''' + requestPerTabelName + '''), &per, TAG_CMM_PER);
}

void SPerPrim''' + requestPerTabelName + '''::JudgeCrossThr( const Octet period, Long64 fid, MPerThr* thr, SEQUENCE<MAlmChssV1>& alm )
{
	NSP_TEMP_UNUSED_ARG(period);
	NSP_TEMP_UNUSED_ARG(fid);
	NSP_TEMP_UNUSED_ARG(thr);
	NSP_TEMP_UNUSED_ARG(alm);
}

void SPerPrim''' + requestPerTabelName + '''::ClearCrossThrAlm( const Octet period, Long64 fid, SEQUENCE<MAlmChssV1>& alm )
{
	NSP_TEMP_UNUSED_ARG(period);
	NSP_TEMP_UNUSED_ARG(fid);
	NSP_TEMP_UNUSED_ARG(alm);
}

void SPerPrim''' + requestPerTabelName + '''::ClearSingleCrossThrAlm(const Octet period, Long64 fid, Short perid, SEQUENCE<MAlmChssV1>& alm)
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
            perToolsCppTemp += '''
	PER_PRIM_INFO(''' + requestPerNameTemp + ''');'''

    perToolsCppTemp += '''
}
#endif'''

    return perToolsCppTemp

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
