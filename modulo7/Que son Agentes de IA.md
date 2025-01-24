# Guía Rápida: Agentes de IA

## ¿Qué es la Arquitectura Cognitiva?
La arquitectura cognitiva define cómo un sistema de IA "piensa" - es decir, el flujo de código/prompts/llamadas a LLM que procesa la entrada del usuario y genera acciones o respuestas. Incluye:
- Flujos de procesamiento
- Patrones de razonamiento
- Gestión de memoria
- Mecanismos de decisión

## Niveles de Autonomía
![autonomy-levels](https://github.com/EPA-Digital/ads-ninja/blob/master/modulo7/Screenshot-2024-06-28-at-7.33.10-PM.png)
### 1. Código Puro
- Todo está hardcodeado
- Sin toma de decisiones dinámica
- Control total pero inflexible

### 2. LLM Simple
- Una sola llamada al LLM
- Algo de preprocesamiento
- Ideal para chatbots básicos

### 3. Cadena de LLMs
- Secuencia de llamadas LLM
- Procesamiento por etapas
- Mejor para tareas complejas

### 4. Router
- Decisiones dinámicas de flujo
- Selección de ruta basada en input
- Agrega imprevisibilidad controlada

### 5. Máquina de Estados
- Combina routing con loops
- Mantiene estado entre llamadas
- Mayor autonomía pero controlada

### 6. Agente Autónomo
- Control total sobre acciones
- Actualiza sus propias instrucciones
- Máxima flexibilidad y autonomía

## ¿Qué es un Agente de IA?
Un agente de IA es un sistema que utiliza modelos de lenguaje (LLMs) para razonar, planear y ejecutar tareas a través de:
- Toma de decisiones autónoma
- Uso de herramientas externas
- Capacidad de reflexión y ajuste
- Interacción con el entorno y humanos

## Arquitecturas Multi-Agente
### 1. Red (Network)
- Cada agente puede comunicarse con cualquier otro
- Decisiones distribuidas
- Mayor flexibilidad pero más complejo de coordinar

### 2. Supervisor
- Un agente central coordina otros agentes
- Control centralizado de decisiones
- Más fácil de gestionar pero posible cuello de botella

### 3. Herramientas (Tool-calling)
- Agentes como herramientas especializadas
- Un supervisor utiliza agentes como funciones
- Bueno para tareas bien definidas

### 4. Jerárquico
- Múltiples niveles de supervisión
- Equipos especializados con sus propios supervisores
- Escalable para problemas complejos

## Patrones de Diseño Comunes

### 1. ReAct (Razonamiento + Acción)
- Ciclo: Pensamiento → Acción → Observación
- Mantiene contexto corto plazo
- Ideal para tareas secuenciales

### 2. Plan & Solve
- Planificación inicial detallada
- Ejecución paso a paso
- Replanificación según necesidad

### 3. Reflexión
- Evaluación continua del progreso
- Aprendizaje de experiencia
- Mejora iterativa de estrategias

## Mejores Prácticas de Implementación

1. **Simplicidad**
   - Comenzar con soluciones simples
   - Agregar complejidad solo cuando sea necesario
   - Mantener flujos claros y rastreables

2. **Transparencia**
   - Documentar decisiones y acciones
   - Mantener registros de comunicación
   - Facilitar supervisión humana

3. **Interoperabilidad**
   - APIs bien definidas
   - Formatos estándar de comunicación
   - Herramientas documentadas

4. **Control**
   - Mecanismos de parada
   - Límites de recursos
   - Puntos de verificación humana

## Cuándo Usar Cada Patrón

### Red (Network)
✅ Problemas que requieren colaboración diversa
❌ Cuando la coordinación es crítica

### Supervisor
✅ Tareas con flujos claros
❌ Cuando se necesita alta autonomía

### Tool-calling
✅ Funciones especializadas y bien definidas
❌ Problemas muy abiertos o creativos

### Jerárquico
✅ Proyectos grandes y complejos
❌ Tareas simples o lineales

## Consideraciones Finales
- Evaluar complejidad vs beneficio
- Priorizar confiabilidad sobre sofisticación
- Mantener el control humano apropiado
- Iterar basado en retroalimentación real

## Referencias
- [what-is-a-cognitive-architecture](https://blog.langchain.dev/what-is-a-cognitive-architecture/)
- [building-effective-agents](https://www.anthropic.com/research/building-effective-agents)
- [design-patterns-an-overview](https://medium.com/binome/ai-agent-workflow-design-patterns-an-overview-cf9e1f609696)
- [multi_agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)