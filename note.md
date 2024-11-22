#### Interactive question answering app 開發紀錄

**參考文件**
網頁
[Flask Tutorial](https://www.geeksforgeeks.org/flask-tutorial/)

Youtube
[CS50x 2024 - Lecture 9 - Flask](https://www.youtube.com/watch?v=-aqUek49iL8)

[Python + JavaScript - Full Stack App Tutorial](https://www.youtube.com/watch?v=PppslXOR7TA)

---

**流程圖**

```mermaid
graph TD;

登入頁面--使用者輸入文字-->前端JS基礎驗證--正確-->後端PYTHON二次驗證--正確-->活動頁面;
前端JS基礎驗證-.錯誤.->登入頁面;
後端PYTHON二次驗證-.錯誤.->登入頁面;
```
