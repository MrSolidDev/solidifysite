export type Service = {
  id: string
  familyId: string
  number: string
  icon: string
  title: string
  tagline: string
  description: string
  deliverables: string[]
  technologies: string[]
}

export type Product = {
  id: string
  familyId: string
  status: string
  icon: string
  title: string
  shortDescription: string
  description: string
  salesFocus: string
  valuePoints: string[]
  features: string[]
  useCases: string[]
  audiences: string[]
}

export type SolutionFamily = {
  id: string
  name: string
  eyebrow: string
  description: string
  icon: string
}

export type CaseStudy = {
  id: string
  serviceIds: string[]
  eyebrow: string
  title: string
  challenge: string
  solution: string
  result: string
  stack: string[]
}

export const productFamilies: SolutionFamily[] = [
  {
    id: 'ollin',
    name: 'Familia Ollin',
    eyebrow: 'Comunicación en movimiento',
    description: 'Soluciones para administrar contenido, activar audiencias y convertir pantallas en experiencias de comunicación inteligentes.',
    icon: 'pi pi-bolt',
  },
]

export const serviceFamilies: SolutionFamily[] = [
  {
    id: 'ingenieria-digital',
    name: 'Ingeniería digital',
    eyebrow: 'Construir y conectar',
    description: 'Servicios para desarrollar sistemas empresariales, integrar plataformas y automatizar la operación.',
    icon: 'pi pi-code',
  },
  {
    id: 'experiencia-estrategia',
    name: 'Experiencias y estrategia',
    eyebrow: 'Diseñar y evolucionar',
    description: 'Servicios para crear experiencias interactivas y convertir necesidades de negocio en rutas tecnológicas claras.',
    icon: 'pi pi-sparkles',
  },
]

export const products: Product[] = [
  {
    id: 'concursos-interactivos',
    familyId: 'ollin',
    status: 'Producto disponible',
    icon: 'pi pi-trophy',
    title: 'Ollin Pulse',
    shortDescription: 'Software para producir concursos por equipos en eventos en vivo, con control centralizado, pantalla pública, contenido configurable y puntuación automatizada.',
    description: 'Convierte una dinámica de preguntas y respuestas en una experiencia visual con ritmo de programa de televisión. Mantiene separados el panel privado de producción y la pantalla que observa el público, para que cada persona tenga la información correcta durante la operación.',
    salesFocus: 'Convierte cualquier trivia en una experiencia de escenario profesional, reutilizable y fácil de operar, sin depender de un desarrollo nuevo para cada evento.',
    valuePoints: [
      'Profesionaliza trivias y concursos en vivo.',
      'Reduce presentaciones, cálculos y controles manuales.',
      'Sincroniza a operador, conductor, participantes y audiencia.',
      'Permite reutilizar la plataforma con nuevos contenidos e identidades.',
    ],
    features: [
      'Panel privado de producción y pantalla pública independiente',
      'Importación de preguntas desde Excel y CSV',
      'Partidas cortas, extendidas y de desempate',
      'Puntuación, multiplicadores, errores y robos automatizados',
      'Revelado progresivo de respuestas y escenas de resultados',
      'Vista previa, línea de tiempo y atajos de teclado',
      'Personalización visual, sonora y de mecánicas',
      'Compatibilidad con proyectores, pantallas LED y monitores',
    ],
    useCases: ['Activaciones de marca', 'Eventos corporativos', 'Capacitaciones', 'Convenciones y ferias'],
    audiences: ['Agencias', 'Productoras', 'Recursos humanos', 'Organizadores de eventos'],
  },
  {
    id: 'ollin-media',
    familyId: 'ollin',
    status: 'Producto disponible',
    icon: 'pi pi-play-circle',
    title: 'Ollin Media',
    shortDescription: 'Plataforma integral para administrar, programar, distribuir y monitorear contenido digital en redes de pantallas desde una operación centralizada.',
    description: 'Transforma pantallas en canales de comunicación inteligentes mediante una plataforma de administración en la nube y reproductores preparados para operar desde una sola ubicación hasta despliegues empresariales de gran escala. Su arquitectura flexible se adapta a comunicación corporativa, publicidad, señalización informativa y experiencias interactivas.',
    salesFocus: 'Conecta contenido, tecnología y audiencia para entregar mensajes relevantes en el momento y lugar adecuados, con control centralizado y sin intervención técnica en cada ubicación.',
    valuePoints: [
      'Centraliza la operación de contenidos y dispositivos.',
      'Actualiza campañas y mensajes de forma remota e inmediata.',
      'Escala desde una pantalla hasta redes en múltiples ubicaciones.',
      'Integra información empresarial y contenido dinámico.',
    ],
    features: [
      'Gestión centralizada de imágenes, videos y páginas web',
      'Programación por horarios, fechas y ubicaciones',
      'Monitoreo en tiempo real de dispositivos y pantallas',
      'Actualizaciones remotas sin intervención en sitio',
      'Administración de múltiples ubicaciones y redes de gran escala',
      'Integración con sistemas empresariales y fuentes externas',
      'Compatibilidad con contenido dinámico y experiencias interactivas',
    ],
    useCases: [
      'Comunicación interna corporativa',
      'Publicidad y promociones en retail',
      'Menús digitales y directorios interactivos',
      'Dashboards y métricas en tiempo real',
      'Centros de monitoreo y videowalls',
      'Eventos y experiencias inmersivas',
    ],
    audiences: ['Corporativos', 'Retail', 'Restaurantes', 'Centros de monitoreo'],
  },
]

export const services: Service[] = [
  {
    id: 'software',
    familyId: 'ingenieria-digital',
    number: '01',
    icon: 'pi pi-desktop',
    title: 'Software empresarial a medida',
    tagline: 'Herramientas que se adaptan a la operación, no al revés.',
    description: 'Diseñamos aplicaciones web para digitalizar flujos, centralizar información y convertir procesos manuales en experiencias simples.',
    deliverables: ['Portales y sistemas internos', 'Dashboards operativos', 'APIs y backends escalables'],
    technologies: ['Vue', 'TypeScript', 'Python', 'AWS'],
  },
  {
    id: 'integraciones',
    familyId: 'ingenieria-digital',
    number: '02',
    icon: 'pi pi-link',
    title: 'Integraciones y automatización',
    tagline: 'Información conectada para tomar mejores decisiones.',
    description: 'Integramos sistemas empresariales y fuentes de datos para reducir tareas repetitivas, errores y puntos ciegos en la operación.',
    deliverables: ['Integraciones SAP y OData', 'Automatización financiera', 'Sincronización con SQL y APIs'],
    technologies: ['SAP', 'OData', 'REST', 'SQL Server'],
  },
  {
    id: 'experiencias',
    familyId: 'experiencia-estrategia',
    number: '03',
    icon: 'pi pi-sparkles',
    title: 'Experiencias interactivas',
    tagline: 'Tecnología digital que responde al mundo físico.',
    description: 'Creamos experiencias para retail y espacios presenciales mediante contenido dinámico, sensores y control de dispositivos.',
    deliverables: ['Digital signage', 'Interacción por sensores', 'Control de iluminación y contenido'],
    technologies: ['QuickplayX', 'Raspberry Pi', 'Nexmosphere', 'Node.js'],
  },
  {
    id: 'consultoria',
    familyId: 'experiencia-estrategia',
    number: '04',
    icon: 'pi pi-compass',
    title: 'Consultoría y evolución digital',
    tagline: 'Claridad técnica antes de invertir en tecnología.',
    description: 'Aterrizamos necesidades de negocio en una ruta técnica viable, con alcance, prioridades y decisiones comprensibles.',
    deliverables: ['Diagnóstico y arquitectura', 'Roadmap de producto', 'Acompañamiento técnico'],
    technologies: ['Discovery', 'Arquitectura', 'Agile', 'Cloud'],
  },
]

export const caseStudies: CaseStudy[] = [
  {
    id: 'finanzas-sap',
    serviceIds: ['software', 'integraciones'],
    eyebrow: 'Operación financiera',
    title: 'Control empresarial conectado con SAP y AWS',
    challenge: 'La información financiera vivía en distintos puntos y requería seguimiento manual para completar procesos internos.',
    solution: 'Una plataforma web modular conectada a servicios OData y funciones en AWS para consultar, validar y procesar información.',
    result: 'Flujos más claros, datos centralizados y una base reutilizable para nuevas herramientas operativas.',
    stack: ['Vue 3', 'TypeScript', 'SAP OData', 'AWS Lambda'],
  },
  {
    id: 'retail-interactivo',
    serviceIds: ['experiencias', 'software'],
    eyebrow: 'Retail y espacios físicos',
    title: 'Contenido que reacciona a cada interacción',
    challenge: 'Las pantallas mostraban contenido estático y no respondían a la presencia o acciones de los visitantes.',
    solution: 'Una experiencia basada en QuickplayX, sensores y controladores para activar contenido, iluminación y secuencias en tiempo real.',
    result: 'Una experiencia diferenciada, administrable y preparada para replicarse en nuevos espacios.',
    stack: ['QuickplayX', 'Sensores PIR', 'Nexmosphere', 'Raspberry Pi'],
  },
  {
    id: 'preventa-b2b',
    serviceIds: ['consultoria', 'software'],
    eyebrow: 'Preventa tecnológica',
    title: 'De necesidades ambiguas a propuestas ejecutables',
    challenge: 'Los proyectos comenzaban con ideas amplias, múltiples involucrados y poca definición técnica.',
    solution: 'Un proceso de discovery, prototipado y documentación para convertir necesidades en alcances, demos y rutas de implementación.',
    result: 'Mejor alineación entre negocio y tecnología, menos incertidumbre y decisiones de inversión más claras.',
    stack: ['Discovery', 'Prototipado', 'Arquitectura', 'Project management'],
  },
]

export const processSteps = [
  { number: '01', title: 'Entender', text: 'Identificamos el problema, las personas involucradas y el resultado que realmente importa.' },
  { number: '02', title: 'Diseñar', text: 'Definimos alcance, arquitectura y una experiencia coherente antes de construir.' },
  { number: '03', title: 'Construir', text: 'Entregamos por etapas visibles para validar temprano y reducir incertidumbre.' },
  { number: '04', title: 'Evolucionar', text: 'Medimos, documentamos y dejamos una base mantenible para el siguiente paso.' },
]
