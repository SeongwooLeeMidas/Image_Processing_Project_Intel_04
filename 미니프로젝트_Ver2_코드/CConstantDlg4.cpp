// CConstantDlg4.cpp: 구현 파일
//

#include "pch.h"
#include "ColorImageAlpha1.h"
#include "afxdialogex.h"
#include "CConstantDlg4.h"


// CConstantDlg4 대화 상자

IMPLEMENT_DYNAMIC(CConstantDlg4, CDialog)

CConstantDlg4::CConstantDlg4(CWnd* pParent /*=nullptr*/)
	: CDialog(IDD_DIALOG4, pParent)
	, m_constant4(0)
{

}

CConstantDlg4::~CConstantDlg4()
{
}

void CConstantDlg4::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT1, m_constant4);
}


BEGIN_MESSAGE_MAP(CConstantDlg4, CDialog)
END_MESSAGE_MAP()


// CConstantDlg4 메시지 처리기
