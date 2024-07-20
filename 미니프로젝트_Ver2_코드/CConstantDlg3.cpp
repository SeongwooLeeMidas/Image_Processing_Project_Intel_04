// CConstantDlg3.cpp: 구현 파일
//

#include "pch.h"
#include "ColorImageAlpha1.h"
#include "afxdialogex.h"
#include "CConstantDlg3.h"


// CConstantDlg3 대화 상자

IMPLEMENT_DYNAMIC(CConstantDlg3, CDialog)

CConstantDlg3::CConstantDlg3(CWnd* pParent /*=nullptr*/)
	: CDialog(IDD_DIALOG3, pParent)
	, m_constant3(0)
{

}

CConstantDlg3::~CConstantDlg3()
{
}

void CConstantDlg3::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT1, m_constant3);
}


BEGIN_MESSAGE_MAP(CConstantDlg3, CDialog)
END_MESSAGE_MAP()


// CConstantDlg3 메시지 처리기
