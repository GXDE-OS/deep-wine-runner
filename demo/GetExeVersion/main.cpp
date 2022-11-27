/**********************************
 * ���ߣ�gfdgd xi��Ϊʲô����ϲ���ܳ�û�Ͱ�����
 * �汾��2.5.0
 * ����ʱ�䣺2022��11��27��
 * ֻ���� Wine/Windows ����
 **********************************/
#include <iostream> 
#include <string>
#include <fstream>
#include <Windows.h>
#pragma comment(lib, "version.lib");
using namespace std;

// �ȿӡ������Ҫ�� Dev CPP ��������ļ�����Ҫ�ڱ���ѡ��� -lversion 
//�����ļ��汾��
//@params:filename:�ļ���
string GetFileVersion(LPCWSTR filename)
{ 
	string asVer = "";
	VS_FIXEDFILEINFO *pVsInfo;
	unsigned int iFileInfoSize = sizeof(VS_FIXEDFILEINFO);
	int iVerInfoSize = GetFileVersionInfoSizeW(filename, NULL); 
	if(iVerInfoSize != 0)
	{ 
		char *pBuf = NULL;

		while(!pBuf)
		{
			pBuf = new char[iVerInfoSize];
		}
		if(GetFileVersionInfoW(filename, 0, iVerInfoSize, pBuf))
		{ 
			if(VerQueryValueA(pBuf, "\\", (void **)&pVsInfo, &iFileInfoSize))
			{ 
				sprintf(pBuf, "%d.%d.%d.%d", HIWORD(pVsInfo->dwFileVersionMS), LOWORD(pVsInfo->dwFileVersionMS), HIWORD(pVsInfo->dwFileVersionLS), LOWORD(pVsInfo->dwFileVersionLS));
				asVer = pBuf; 
			} 
		} 
		delete pBuf;
	}
	return asVer;
}

// ��ʽת�� 
LPWSTR ConvertCharToLPWSTR(const char* szString)
{
	int dwLen = strlen(szString) + 1;
	int nwLen = MultiByteToWideChar(CP_ACP, 0, szString, dwLen, NULL, 0);//������ʵĳ���
	LPWSTR lpszPath = new WCHAR[dwLen];
	MultiByteToWideChar(CP_ACP, 0, szString, dwLen, lpszPath, nwLen);
	return lpszPath;
}

int main(int argc, char* argv[]){
	if (argc < 2){
		cout << "Unfull Option" << endl;
		return 1;
	}
	string version = GetFileVersion(ConvertCharToLPWSTR(argv[1]));
	cout << "Version: " << version << endl;
	if (argc == 3){
		cout << "Write To " << argv[2] << endl;
		// Ϊ�˷����ȡ��д���ı��ĵ� 
		ofstream write(argv[2], ios::trunc);
		write << version;
		write.close();
	}
	return 0;
}
