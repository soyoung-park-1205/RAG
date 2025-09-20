<h1>Ollama와 네이버 검색 API를 활용한 RAG 시스템 구축</h1>
<h3>현재 System Architecture (Mermaid로 표현)</h3>
<img width="500" alt="Image" src="https://github.com/user-attachments/assets/b205f3e5-66a5-4cb2-adb2-4ea9f1aed38d" />

</br><h3>Key Technologies</h3>
| Category      | Details                 |
|---------------|-------------------------|
| **Language**  | Python, HTML            |
| **Framework** | Flask                   |
| **Library**   | LangGraph               |
| **Tool**      | Ollama                  |
| **Models**    | gpt-oss:20b, Gemma 3:1b    |

</br><h3>환경 구축</h3>
1. Ollama를 활용하여 로컬 환경에서 gemma3, llama3.2 LLM 모델 구동 환경을 구축</br>
2. LangGraph를 활용해 RAG 시스템 구축 (LangChain(V1)에서 변경)
3. MemorySaver로 이전 대화 기억

</br><h3>Node 세부 설명</h3>
1. needs_search: 검색 필요 여부를 판단하는 conditional_edge </br>
2. extract_keyword: Kkma 라이브러리로 질문에서 핵심 키워드 추출 </br>
3. naver_searcher: 네이버 검색 API로 핵심 키워드에 대한 검색 결과를 가져옴 </br>
4. relevance_check: 질문, 검색된 문서 간의 관련성 체크 </br>
5. llm_answer: 질문에 대한 LLM의 단순 답변 </br>
6. llm_answer_search: 검색 내용을 활용하여 LLM 답변 </br>

</br><h3>활용 예시</h3>
<img width="350" alt="Image" src="https://github.com/user-attachments/assets/7a8a9260-642a-45ce-8016-8819088abfd5" />
