
// ColorImageAlpha1View.h: CColorImageAlpha1View 클래스의 인터페이스
//

#pragma once


class CColorImageAlpha1View : public CView
{
protected: // serialization에서만 만들어집니다.
	CColorImageAlpha1View() noexcept;
	DECLARE_DYNCREATE(CColorImageAlpha1View)

// 특성입니다.
public:
	CColorImageAlpha1Doc* GetDocument() const;

// 작업입니다.
public:

// 재정의입니다.
public:
	virtual void OnDraw(CDC* pDC);  // 이 뷰를 그리기 위해 재정의되었습니다.
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
protected:
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);

// 구현입니다.
public:
	virtual ~CColorImageAlpha1View();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// 생성된 메시지 맵 함수
protected:
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnEqualImage();
	afx_msg void OnGrayScale();
	afx_msg void OnChangeSatur();
	afx_msg void OnPickOrange();
	afx_msg void OnEmboss();
	afx_msg void OnEmbossHsi();
	afx_msg void OnAddImage();
	afx_msg void OnReverseImage();
	afx_msg void OnDarkImage();
	afx_msg void OnBlackImage();
	afx_msg void OnGammaImage();
	afx_msg void OnParabolCap();
	afx_msg void OnParabolCup();
	afx_msg void OnAndImage();
	afx_msg void OnOrImage();
	afx_msg void OnXorImage();
	afx_msg void OnZoomOut();
	afx_msg void OnZoomIn();
	afx_msg void OnZoomIn2();
	afx_msg void OnRotate();
	afx_msg void OnRotate2();
	afx_msg void OnHistoStretch();
	afx_msg void OnEndIn();
	afx_msg void OnHistoEqual();
	afx_msg void OnBlur();
	afx_msg void OnBlurHsi();
	afx_msg void OnSharp();
	afx_msg void OnSharpHsi();
	afx_msg void OnEdge1();
	afx_msg void OnEdge2();
	afx_msg void OnEdgeHsi();
	afx_msg void OnEdge2Hsi();
	afx_msg void OnLaplacian1();
	afx_msg void OnLaplacian1Hsi();
	afx_msg void OnLaplacian2();
	afx_msg void OnLaplacian2Hsi();
	afx_msg void OnLaplacian3();
	afx_msg void OnLaplacian3Hsi();
	afx_msg void OnGausians();
	afx_msg void OnGausiansHsi();
	afx_msg void OnPrewitt1();
	afx_msg void OnPrewitt1Hsi();
	afx_msg void OnPrewitt2();
	afx_msg void OnPrewitt2Hsi();
	afx_msg void OnSobel1();
	afx_msg void OnSobel1Hsi();
	afx_msg void OnSobel2();
	afx_msg void OnSobel2Hsi();
};

#ifndef _DEBUG  // ColorImageAlpha1View.cpp의 디버그 버전
inline CColorImageAlpha1Doc* CColorImageAlpha1View::GetDocument() const
   { return reinterpret_cast<CColorImageAlpha1Doc*>(m_pDocument); }
#endif

