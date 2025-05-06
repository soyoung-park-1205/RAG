<h1>Ollama와 네이버 검색 API를 활용한 RAG 시스템 구축</h1>

<h3>System Architecture</h3>
<img src="https://github.com/user-attachments/assets/294655b5-40b1-4c1c-bd05-115137fa99e0" width="800" height="400"/>

</br><h3>Key Technologies</h3>
| Category      | Details                 |
|---------------|-------------------------|
| **Language**  | Python, HTML            |
| **Framework** | Flask                   |
| **Library**   | LangChain               |
| **Tool**      | Ollama                  |
| **Models**    | Llama 3.2, Gemma 3.1    |

</br><h3>환경 구축</h3>
1. Ollama를 활용하여 로컬 환경에서 gemma3, llama3.2 LLM 모델 구동 환경을 구축</br>
2. LangChain을 활용해 RAG 시스템 구축

</br><h3>RAG 응답 프로세스</h3>
1. Kkma 라이브러리로 질문에서 핵심 키워드 추출 </br>
2. 네이버 검색 API로 핵심 키워드에 대한 검색 결과를 가져옴 </br>
3. 질문 + 검색 결과로 gemma3, llama3.2 모델의 응답 결과를 가져옴 </br>

</br><h3>활용 예시</h3>
<img src="https://github.com/user-attachments/assets/6eb7ffb5-af21-4396-8711-1e2b106cb899" width="700" height="450"/>
