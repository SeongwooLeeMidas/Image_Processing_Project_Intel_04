#pragma once
#include "afxdialogex.h"


// CConstantDlg3 대화 상자

class CConstantDlg3 : public CDialog
{
	DECLARE_DYNAMIC(CConstantDlg3)

public:
	CConstantDlg3(CWnd* pParent = nullptr);   // 표준 생성자입니다.
	virtual ~CConstantDlg3();

// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_DIALOG3 };
#endif

protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

	DECLARE_MESSAGE_MAP()
public:
	double m_constant3;
};
