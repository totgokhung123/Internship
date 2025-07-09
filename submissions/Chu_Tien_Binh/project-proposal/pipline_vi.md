flowchart TD
  subgraph "📤 Document Upload"
    A[Web Upload] -->|PDF/Image| B[S3: documents<br/>Standard-IA]
    B -->|Event| C[SQS: processing-queue]
  end

  subgraph "🔍 OCR & Extraction"
    C --> D[Lambda: Textract Handler<br/>1GB RAM, 5min]
    D -->|Extract text| E[Textract API<br/>FREE: 1000 pages/month]
    E --> F[Lambda: Text Processing<br/>512MB RAM, 1min]
  end

  subgraph "🧠 NLP Analysis"
    F --> G[Lambda: NLP Pipeline<br/>2GB RAM, 2min]
    G -->|Named Entity Recognition| H[spaCy Model]
    G -->|Key-Value Extraction| I[Regex + Rules]
    G -->|Classification| J[scikit-learn]
  end

  subgraph "💾 Storage & Search"
    G --> K[DynamoDB: documents<br/>On-Demand]
    K --> L[OpenSearch Serverless<br/>FREE: 5GB]
    M[API Gateway] --> N[Lambda: Search API]
    N --> L
  end

  subgraph "📊 Analytics Dashboard"
    O[CloudWatch] --> P[Lambda: Analytics]
    P --> Q[S3: reports]
    R[Web Dashboard] --> M
  end
