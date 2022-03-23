# 1. HTML

**Hyper Text Markup Language**

* **Hyper Text**: 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

* **Markup Language**: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

  ex) HTML, Markdown

=> **"웹 페이지를 작성하기 위한 언어"**



##  1.1. 기본구조

* html: 문서의 최상위 요소
* head: 문서 메타데이터 요소
  * 문서제목, 인코딩, 스타일, 외부 파일 로딩 등
  * 일반적으로 브라우저에 나타나지 않는 내용
  * ex): \<title\>: 브라우저 상단 타이틀 \<meta\> \<link\> \<script\> \<style\>
* body: 문서 본문 요소
  * 실제 화면 구성과 관련된 내용

* DOM: document Object Model
  * 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기위한 구조
    * HTML 문서에 대한 모델을 구성함
    * HTML 문서 내의 각 요소에 접근/ 수정에 필요한 프로퍼티와 메서드를 제공함







\<b\> : 그냥 굴게, \<strong\>: 강조의 의미를 담음 ...?  => 기능적으로 똑같고 출력되는것도 똑같음