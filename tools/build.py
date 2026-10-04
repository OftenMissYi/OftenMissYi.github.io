"""Build the static portfolio with one shared case-study template. Python stdlib only."""
from pathlib import Path
from html import escape as e

ROOT = Path(__file__).resolve().parents[1]
GITHUB = 'https://github.com/OftenMissYi/'

PROJECTS = [
    dict(slug='uav-path-planning', title='UAV Path Planning & Trajectory Control', category='Motion planning & control',
         repo='UAV-Path-Planning-and-Trajectory-Control', image='images/uav-path-planning.jpg',
         alt='UAV trajectory and tracking plots from the MATLAB simulation',
         summary='From discrete waypoints to smooth flight trajectories. Team leadership and primary implementation of a Minimum-Snap trajectory generator.',
         period='Dec 2025 – Jan 2026', role='Team leader; Minimum-Snap implementation lead', validation='MATLAB simulation',
         tags=['MATLAB', 'A* / Theta*', 'Minimum Snap', 'PID'],
         overview='A team course project at Chongqing University connecting geometric path planning, continuous trajectory generation and UAV control. The work progressed through reference tracking, 3D path search, altitude shaping and trajectory optimization.',
         contribution=['Coordinated the team and contributed across all four project tasks.',
                       'Led the Minimum-Snap implementation using seventh-order polynomials and quadratic optimization.',
                       'Integrated the generated reference states with a provided PID controller and contributed to planning experiments and the final report.'],
         steps=[('Track a reference path', 'Allocate a 25-second trajectory in proportion to segment lengths, generate position and velocity references, and derive yaw from the direction of motion.'),
                ('Search a 3D environment', 'Compare six-neighbor A* with Theta*, whose line-of-sight checks allow arbitrary-angle connections between nodes. Add a progress-dependent altitude penalty to shape vertical motion.'),
                ('Optimize the trajectory', 'Minimize the integral of squared snap, the fourth derivative of position. Solve the seventh-order polynomial coefficients with MATLAB quadprog under waypoint and continuity constraints through jerk.'),
                ('Connect planning to control', 'Perform optimization at initialization, then evaluate position, velocity and acceleration at each time query for the provided tracking controller.')],
         results='The saved complex-environment comparison shows the trade-off clearly: Theta* produced a shorter path with fewer waypoints, while taking longer to plan. The repository documents all four simulation tasks and their tracking plots.',
         note='The 26.3% reduction in path length applies to this reported scenario. Results come from the original project report; physical flight validation was outside the project.',
         table=True,
         gallery=[('images/uav/minimum-snap.jpg', 'Minimum-Snap trajectory generation and simulated tracking.', True),
                  ('images/uav/astar.jpg', 'A* planning and tracking in the complex environment. Final report, Figure 3.4.', True),
                  ('images/uav/theta-star.png', 'Theta* planning and tracking in the same task. Final report, Figure 3.5.', True)],
         resources=[('Final report (Chinese)', 'blob/main/docs/Final-Report.pdf')]),
    dict(slug='motor-imagery-bci', title='Motor Imagery BCI', category='Machine learning & signal processing',
         repo='Motor-Imagery-BCI', image='images/motor-imagery-bci/features.png',
         alt='Eight wavelet-packet coefficient plots extracted from a saved EEG signal',
         summary='Making EEG features visible. Wavelet-packet feature extraction and visualization for a collaborative four-class motor-imagery classification workflow.',
         period='Apr – May 2025', role='Wavelet-packet feature extraction & visualization lead', validation='Offline EEG experiments',
         tags=['Python', 'PyWavelets', 'MNE', 'CSP', 'PyTorch'],
         overview='The project explored how EEG recorded during imagined movement can be represented and classified. Using BCI Competition IV 2a, the team investigated left-hand, right-hand, feet and tongue imagery, alongside model experiments with DeepConvNet, EEGNet, FBCNet and EEG-Conformer.',
         contribution=['Led the wavelet-packet feature extraction and visualization work in Python and PyWavelets.',
                       'Produced a fixed-size feature representation and coefficient plots for inspecting the extraction process.',
                       'Contributed to the collaborative preprocessing, WPD/CSP classification workflow and experiment analysis.'],
         steps=[('Prepare the EEG', 'Load labeled GDF recordings with MNE, filter at 7–35 Hz, exclude EOG channels and extract cue-aligned epochs.'),
                ('Extract wavelet-packet features', 'Apply level-5 Daubechies 4 decomposition. Eight selected nodes contribute 30 coefficients each, producing a tensor shaped (8, trials, channels, 30). Frequency labels account for the difference between natural tree order and frequency order.'),
                ('Apply spatial filtering', 'Fit four CSP components per node using the training split and standardize the resulting 32 features.'),
                ('Train and inspect', 'Train a PyTorch MLP for the four imagery classes and record held-out metrics. The historical protocol used ten repeated random 80/20 splits within a recording.')],
         results='The curated repository brings together the feature module, selected plots, the original team presentation and saved classification records. The feature implementation was checked against the original scripts, and the classifier completed a short execution check on A01T data.',
         note='Historical records lack complete run metadata. The saved training plot is evidence of an original experiment, not a newly reproduced cross-session benchmark. This was offline signal analysis, without real-time device control.',
         gallery=[('images/motor-imagery-bci/features.png', 'Eight selected wavelet-packet nodes from the project’s saved EEG signal.', True),
                  ('images/motor-imagery-bci/training.png', 'Historical WPD/CSP/MLP run: loss, accuracy and Cohen’s kappa over 300 epochs.', True)],
         resources=[('Team presentation (Chinese)', 'blob/main/docs/presentation-zh.pdf'), ('Evaluation notes', 'blob/main/results/README.md')]),
    dict(slug='exoskeleton', title='Bionic Lower-Limb Exoskeleton', category='Mechanical design & mechatronics',
         repo='Bionic-Lower-Limb-Exoskeleton-Integrated-Joint', image='images/exoskeleton/exploded-assembly.jpg',
         alt='Exploded mechanical assembly of the exoskeleton integrated joint',
         summary='An integrated knee-joint drive, developed through motor selection, gearbox design, mechanical integration and structural and dynamic analysis.',
         period='Dec 2025 – May 2026', role='Joint drive design & mechanical analysis', validation='CAD, FEA & dynamic simulation',
         tags=['SolidWorks', 'ANSYS Workbench', 'MSC Adams'],
         overview='An integrated knee-joint drive unit for a bionic lower-limb exoskeleton. The design combines the motor, planetary transmission and supporting structure into a compact assembly, balancing torque requirements with packaging and mechanical performance.',
         contribution=['Worked on motor selection and gearbox design for the integrated joint drive.',
                       'Developed the mechanical assembly and examined how the drive components fit within the knee-joint module.',
                       'Performed structural and performance analysis using ANSYS Workbench and MSC Adams.'],
         steps=[('Select the drive components', 'Consider torque, speed, power and integration constraints when selecting the motor and reduction system.'),
                ('Integrate the joint', 'Model the motor, planetary gears and structural components as a compact assembly. Use exploded and sectional views to examine the internal arrangement.'),
                ('Evaluate structural response', 'Study stress, strain and deformation under modeled loading conditions, including the documented 21 Nm and 55 Nm load cases.'),
                ('Study transmission dynamics', 'Inspect motor torque, output angular velocity, gear-mesh forces and transmission error in MSC Adams.')],
         results='The project produced a mechanical design supported by CAD assembly views, finite-element results and transmission dynamics plots. Together, these artifacts show the progression from component integration to structural and drive-system evaluation.',
         note='Validation is based on CAD, finite-element analysis and transmission simulation. The gallery documents the modeled load cases and mechanical responses.',
         gallery=[('images/exoskeleton/cad-model.jpg', 'CAD model of the integrated joint drive.', False),
                  ('images/exoskeleton/sectional-view.jpg', 'Sectional view of the internal transmission arrangement.', False),
                  ('images/exoskeleton/ansys-von-mises-21nm.jpg', 'Equivalent stress under the modeled 21 Nm loading condition.', False),
                  ('images/exoskeleton/ansys-von-mises-55nm.jpg', 'Equivalent stress under the modeled 55 Nm loading condition.', False)],
         extra=[('images/exoskeleton/structure-replacement.jpg','Structural design and component arrangement.',False),
                ('images/exoskeleton/exploded-assembly.jpg','Exploded view of the joint assembly.',False),
                ('images/exoskeleton/ansys-total-deformation.jpg','Finite-element total deformation.',False),
                ('images/exoskeleton/ansys-strain.jpg','Finite-element strain distribution.',False),
                ('images/exoskeleton/adams-input-torque.jpg','Applied dynamic input torque.',False),
                ('images/exoskeleton/adams-output-velocity.jpg','Planetary carrier output angular velocity.',False),
                ('images/exoskeleton/adams-motor-torque.jpg','Motor driving torque response.',False),
                ('images/exoskeleton/adams-sun-planet-force.jpg','Sun / planet gear mesh force.',False),
                ('images/exoskeleton/adams-planet-ring-force.jpg','Planet / ring gear mesh force.',False),
                ('images/exoskeleton/adams-transmission-error.jpg','Simulated transmission error.',False)],
         resources=[]),
    dict(slug='underwater', title='Underwater Robot', category='Embedded systems & hardware integration',
         repo='Underwater-Robot-STM32F429', image='images/underwater.jpg',
         alt='Underwater robot assembly with propulsion and electrical components',
         summary='Electrical integration and STM32 control development for an underwater robot, with remote-controlled movement and gripper operation tested in water.',
         period='Jun – Aug 2024', role='Electrical & control engineering team member', validation='In-water movement & gripper tests',
         tags=['STM32F429', 'C', 'PWM', 'Hardware integration'],
         overview='A team-built underwater robot with embedded motion and gripper control. My work focused on the electrical interfaces, hardware integration and further development of STM32 software based on an existing control framework.',
         contribution=['Took responsibility for electrical and control engineering within the team, including electrical interfacing and hardware integration.',
                       'Extended the existing STM32 control software to support robot movement and gripper operation.',
                       'Participated in in-water testing to validate remote-controlled movement and the gripper.'],
         steps=[('Organize the electronics', 'Define the component layout and electrical interfaces within the robot enclosure, accounting for installation space and accessibility.'),
                ('Integrate hardware and control', 'Connect the embedded controller with the motion actuators and gripper, building on the project’s existing control framework.'),
                ('Develop actuator behavior', 'Extend STM32 software for the movement and gripper functions needed during remote operation.'),
                ('Test in water', 'Check commanded movement and gripper operation on the physical robot under in-water test conditions.')],
         results='The robot demonstrated remote-controlled movement and gripper operation during in-water tests. The electrical models, installation layout and architecture drawing document the hardware and control context behind that work.',
         note='The architecture diagram provides the wider team context. This case study focuses on electrical integration and the STM32 movement and gripper functions verified during in-water testing.',
         gallery=[('images/underwater/control-architecture.jpg','Wider team control architecture, showing the relationship between onboard computing, embedded control and actuators.',True),
                  ('images/underwater/electrical-model.jpg','Parametric model of the electrical equipment.',False),
                  ('images/underwater/electrical-installation.jpg','Electrical component installation arrangement.',False),
                  ('images/underwater/electrical-layout.jpg','Physical layout of the electrical equipment.',True)],
         resources=[]),
]

def link(url, label, cls=''):
    external = ' target="_blank" rel="noopener noreferrer"' if url.startswith('https:') else ''
    return f'<a href="{e(url)}" class="{cls}"{external}>{e(label)}</a>'

def tags(items):
    return '<div class="tags">' + ''.join(f'<span>{e(t)}</span>' for t in items) + '</div>'

def shell(title, description, content, page='index.html'):
    prefix = '' if page == 'index.html' else 'index.html'
    nav = ''.join(link(prefix+'#'+anchor, text, 'nav-contact' if anchor=='contact' else '') for anchor,text in [('projects','Work'),('about','About'),('experience','Experience'),('contact','Contact')])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Jiayi Zhao</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#12283c"><link rel="canonical" href="https://oftenmissyi.github.io/{'' if page=='index.html' else page}">
<meta property="og:title" content="{e(title)} | Jiayi Zhao"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="assets/space-grotesk.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="assets/site.css"><script src="assets/site.js" defer></script></head><body>
<a class="skip" href="#main">Skip to content</a><header class="site-header wrap">
<a href="index.html" class="brand" aria-label="Jiayi Zhao home"><span class="brand-mark" aria-hidden="true">JZ</span>Jiayi Zhao</a>
<button class="menu-toggle" type="button" aria-controls="navigation" aria-expanded="false">Menu</button>
<nav class="nav-links" id="navigation" aria-label="Main navigation">{nav}</nav></header>
<main id="main">{content}</main><footer class="site-footer wrap"><span>© 2026 Jiayi Zhao</span><span>Robotics, from algorithms to hardware.</span><a href="#main">Back to top</a></footer></body></html>'''

def figure(item):
    src, caption, wide = item
    return f'<figure class="{"wide" if wide else ""}"><a href="{src}" target="_blank" rel="noopener noreferrer" aria-label="Open full-size image: {e(caption)}"><img src="{src}" alt="{e(caption)}" loading="lazy" decoding="async"></a><figcaption>{e(caption)}</figcaption></figure>'

def case_study(p, next_p):
    facts = ''.join(f'<div><dt>{label}</dt><dd>{e(p[key])}</dd></div>' for label,key in [('Period','period'),('My role','role'),('Validation','validation')])
    navigation = ''.join(link('#'+id, label) for id,label in [('overview','Overview'),('contribution','My contribution'),('approach','Approach'),('results','Results'),('gallery','Project gallery'),('resources','Source & tools')])
    contributions = ''.join(f'<li>{e(s)}</li>' for s in p['contribution'])
    steps = ''.join(f'<li><h3>{e(title)}</h3><p>{e(text)}</p></li>' for title,text in p['steps'])
    table = '''<div class="table-wrap"><table><caption>Original final report, Table 3.1: complex-environment simulation</caption><thead><tr><th scope="col">Metric</th><th scope="col">A*</th><th scope="col">Theta*</th></tr></thead><tbody><tr><th scope="row">Waypoints</th><td>19</td><td>7</td></tr><tr><th scope="row">Path length</th><td>18.0000</td><td>13.2594</td></tr><tr><th scope="row">Planning time</th><td>0.012948 s</td><td>0.031532 s</td></tr></tbody></table></div>''' if p.get('table') else ''
    gallery = '<div class="gallery">'+''.join(map(figure,p['gallery']))+'</div>'
    if p.get('extra'):
        gallery += '<details class="gallery-extra"><summary>Explore additional CAD and simulation figures</summary><div class="gallery">'+''.join(map(figure,p['extra']))+'</div></details>'
    resources = link(GITHUB+p['repo'], 'View repository', 'button primary') + ''.join(link(GITHUB+p['repo']+'/'+url,label,'button') for label,url in p['resources'])
    content = f'''<div class="wrap"><div class="breadcrumb">{link('index.html#projects','Selected work')} / Case study</div>
<div class="case-hero"><div><div class="category">{e(p['category'])}</div><h1>{e(p['title'])}</h1><p class="intro">{e(p['summary'])}</p><div class="buttons">{link('#contribution','Explore my contribution','button primary')}{link(GITHUB+p['repo'],'GitHub','button')}</div></div>
<figure class="case-cover"><img src="{p['image']}" alt="{e(p['alt'])}" fetchpriority="high"><figcaption>{e(p['validation'])} / Project artifact</figcaption></figure></div>
<dl class="case-facts">{facts}</dl><div class="case-layout"><nav class="case-nav" aria-label="On this page">{navigation}</nav><div>
<section id="overview" class="case-section"><h2>The project</h2><p>{e(p['overview'])}</p></section>
<section id="contribution" class="case-section"><h2>My contribution</h2><ul class="contribution-list">{contributions}</ul></section>
<section id="approach" class="case-section"><h2>Engineering approach</h2><ol class="steps">{steps}</ol></section>
<section id="results" class="case-section"><h2>Results & validation</h2><p>{e(p['results'])}</p>{table}<div class="result-note"><p>{e(p['note'])}</p></div></section>
<section id="gallery" class="case-section"><h2>Project gallery</h2><p class="small-note">Original project figures. Select an image to view it at full size.</p>{gallery}</section>
<section id="resources" class="case-section"><h2>Source & tools</h2><p>Explore the project files, technical documentation and supporting materials.</p>{tags(p['tags'])}<div class="buttons">{resources}</div></section>
</div></div><aside class="case-bottom"><div><p>Continue exploring</p><h2>{e(next_p['title'])}</h2></div>{link(next_p['slug']+'.html','Next case study','button light')}</aside></div>'''
    return shell(p['title'], p['summary'], content, p['slug']+'.html')

def trajectory_art():
    # Original vector drawing: a conceptual robot motion path, not simulation data.
    grid = ''.join(f'<path d="M{70+i*34} {315-i*16}l250 120M{70+i*34} {315+i*16}l250 -120"/>' for i in range(8))
    return f'''<div class="hero-art"><svg viewBox="0 0 500 460" role="img" aria-labelledby="art-title art-description"><title id="art-title">From sensing to motion</title><desc id="art-description">Conceptual engineering illustration of a robot trajectory through a three-dimensional workspace.</desc>
<defs><pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".7" fill="#526c84"/></pattern></defs>
<circle cx="250" cy="220" r="190" fill="url(#dots)"/><g stroke="#486077" stroke-width=".7" fill="none" opacity=".65">{grid}</g>
<g fill="none" stroke="#7694ae" stroke-width="1"><path d="M78 316V147M78 316l271 128M78 316l261-123"/><path d="M73 154l5-7 5 7M340 435l9 9-12-1M329 194l10-1-6 8"/></g>
<g font-family="Space,sans-serif" font-size="12" fill="#aec4d7"><text x="66" y="136">z</text><text x="357" y="451">x</text><text x="347" y="194">y</text></g>
<g stroke="#7694ae" stroke-width="1.3"><path d="M172 292v-99l66-31 57 27v99l-66 31Z" fill="#203d56"/><path d="M172 193l57 27 66-31M229 220v99" fill="none"/><path d="M302 314v-66l42-20 44 21v66l-42 20Z" fill="#203d56"/><path d="M302 248l44 21 42-20M346 269v66" fill="none"/></g>
<path d="M111 325C113 267 122 227 151 190S243 96 300 118s60 90 92 84" fill="none" stroke="#496782" stroke-width="1.5" stroke-dasharray="5 7"/>
<path d="M111 325C99 237 131 129 201 108S289 130 300 172s42 64 92 30" fill="none" stroke="#6c9fff" stroke-width="4" stroke-linecap="round"/>
<g fill="#12283c" stroke="#a9c7ff" stroke-width="2"><circle cx="111" cy="325" r="6"/><circle cx="201" cy="108" r="5"/><circle cx="300" cy="172" r="5"/><circle cx="392" cy="202" r="6"/></g>
<g transform="translate(289 148) rotate(24)" fill="none" stroke="#f4a261" stroke-width="2"><path d="M-25-13L25 13M-25 13L25-13"/><ellipse cx="-28" cy="-15" rx="16" ry="6"/><ellipse cx="28" cy="15" rx="16" ry="6"/><ellipse cx="-28" cy="15" rx="16" ry="6"/><ellipse cx="28" cy="-15" rx="16" ry="6"/><path d="M-9-7h18v14H-9Z" fill="#12283c"/></g>
<g font-family="Space,sans-serif" font-size="12" fill="#d3e2f0"><text x="79" y="355">sense</text><text x="162" y="81">plan</text><text x="393" y="232">act</text></g></svg><div class="art-caption"><span>Perception → planning → control</span><span>Concept sketch</span></div></div>'''

def homepage():
    cards = ''
    for p in PROJECTS:
        cards += f'''<article class="project-card"><div class="project-visual"><img src="{p['image']}" alt="{e(p['alt'])}" loading="lazy" decoding="async"></div><div class="project-copy"><div class="category">{e(p['category'])}</div><h3><button class="project-toggle" type="button" aria-expanded="true" aria-controls="panel-{p['slug']}">{e(p['title'])}<span class="expand-mark" aria-hidden="true">+</span></button></h3><div class="project-detail" id="panel-{p['slug']}"><p>{e(p['summary'])}</p>{tags(p['tags'])}<div class="project-links">{link(p['slug']+'.html','Read case study')}{link(GITHUB+p['repo'],'GitHub')}</div></div></div></article>'''
    content = f'''<div class="wrap"><section class="hero" aria-labelledby="home-title"><div><div class="role">Robotics engineer · M.Sc. student at TUM</div><h1 id="home-title">Hi, I’m<br>Jiayi Zhao.</h1><p class="intro">I work where intelligent algorithms meet physical machines.</p><p class="bio">From UAV trajectories and EEG signals to embedded controllers and mechanical joints, I connect software, control and hardware to make robotic systems work.</p><div class="buttons">{link('#projects','Explore my work','button primary')}{link('#about','Get to know me','button')}</div></div>{trajectory_art()}</section>
<div class="profile-strip"><a href="#experience"><strong>Learning at TUM</strong><span>M.Sc. Robotics, Cognition, Intelligence</span><p class="profile-clue">From a B.Eng. in Robotics Engineering at Chongqing University to graduate study in Garching, Germany.</p></a><a href="#skills"><strong>Connecting disciplines</strong><span>Algorithms, control and hardware</span><p class="profile-clue">Python and MATLAB for algorithms. STM32 for control. CAD and simulation for the mechanics.</p></a><a href="#contact"><strong>Across languages</strong><span>English C1 · German C1 · Chinese native</span><p class="profile-clue">Based in Garching, Germany. Get in touch to discuss robotics, research or engineering opportunities.</p></a></div>
<section class="section" id="projects"><div class="section-head"><h2>Selected work</h2><p>Explore a project to bring it into focus. From algorithms to the systems they drive.</p></div><div class="projects-grid">{cards}</div>
<div class="more-projects"><h3>More engineering projects</h3>
<article class="repo-row"><img src="images/swiftpicker.jpg" alt="SwiftPicker mobile manipulator simulation" loading="lazy"><div><h3>ROS Autonomous Robot — SwiftPicker</h3><p>LiDAR navigation and MoveIt manipulation with existing robot models. Target navigation and 6-DOF grasping tested in Gazebo and RViz.</p></div>{link(GITHUB+'ROS-Autonomous-Robot-SwiftPicker','View on GitHub','text-link')}</article>
<article class="repo-row"><img src="images/mobile-robot.jpg" alt="STM32 mobile robot" loading="lazy"><div><h3>Autonomous Mobile Robot</h3><p>Independently developed STM32 firmware for motor control, ultrasonic obstacle avoidance, Bluetooth commands and audio, validated on a physical robot.</p></div>{link(GITHUB+'Autonomous-Mobile-Robot-STM32','View on GitHub','text-link')}</article>
<article class="repo-row coming-soon"><img src="images/vision-robot.jpg" alt="Vision-based robot project" loading="lazy"><div><h3>Vision-Based Robot</h3><p>OpenCV color and lane detection with motion-control logic. Project write-up in preparation.</p></div><span class="status">Coming soon</span></article>
</div></section></div>
<section id="about" class="section about-band"><div class="wrap about-grid"><div><div class="about-label">A little about me</div><h2>Thinking in systems.<br>Building across disciplines.</h2></div><div><p>I’m a Robotics Engineering graduate from Chongqing University, now studying Robotics, Cognition, Intelligence at the Technical University of Munich.</p><p>I enjoy the connections between disciplines: how a planner becomes a trackable trajectory, how a signal becomes a useful feature, and how software commands become physical movement.</p><p>My projects span machine learning, motion planning, embedded development and mechanical design. Industry internships have also given me experience with automation, robotic-arm design and engineering documentation.</p></div></div></section>
<div class="wrap"><section class="section journey-grid" id="experience"><div><h2>Education</h2><div class="timeline"><article class="timeline-item"><div class="date">Oct 2026 – Present</div><h3>M.Sc. Robotics, Cognition, Intelligence</h3><div class="institution">Technical University of Munich</div><p>Academic focus: robot learning and control, motion planning, machine learning and 3D computer vision.</p></article><article class="timeline-item"><div class="date">Sep 2022 – Jun 2026</div><h3>B.Eng. Robotics Engineering</h3><div class="institution">Chongqing University</div><p>Intelligent Robotics Track<br>Overall average: <strong>86.36 / 100</strong></p></article></div></div>
<div><h2>Industry experience</h2><div class="timeline"><article class="timeline-item"><div class="date">Jun – Aug 2025 & Oct 2025 – Jan 2026</div><h3>Robotics & Automation Intern</h3><div class="institution">Guizhou Aerospace Wujiang Mechanical & Electrical Equipment Co., Ltd.</div><p>Contributed to an automated loading and unloading system, including mechanical design and motion simulation of a robotic arm.</p><p>Supported electrical and PLC-related engineering tasks and technical documentation for supercritical fluid technology.</p></article></div></div></section>
<section class="section skills-section" id="skills"><div class="section-head"><h2>What I work with</h2><p>Practical skills developed through simulation, code and hands-on integration.</p></div><div class="skills-grid">
<div class="skill-block"><h3>Planning & robotics</h3><p>Path search, trajectory optimization, navigation and simulated manipulation.</p><p class="tools">MATLAB, ROS, MoveIt, Gazebo, RViz</p></div>
<div class="skill-block"><h3>Learning & perception</h3><p>EEG features, classification experiments and computer vision.</p><p class="tools">Python, PyTorch, scikit-learn, MNE, PyWavelets, OpenCV</p></div>
<div class="skill-block"><h3>Embedded & control</h3><p>Motor control, sensor interfaces, serial communication and physical testing.</p><p class="tools">C / C++, STM32, PWM, UART, Keil, STM32CubeMX</p></div>
<div class="skill-block"><h3>Mechanical & industrial</h3><p>Drive integration, structural analysis, motion simulation and automation.</p><p class="tools">SolidWorks, Siemens NX, ANSYS, Adams, TIA Portal</p></div></div>
<div class="recognition"><div><h3>Recognition</h3><div class="award"><time>2024</time><div>Engineering Practice & Innovation Competition<small>Third Prize, university level · Chongqing University</small></div></div><div class="award"><time>2023</time><div>Academic Excellence Scholarship<small>Second Prize · Chongqing University</small></div></div></div><div><h3>Languages</h3><div class="languages"><div><strong>English</strong><span>C1</span></div><div><strong>German</strong><span>C1</span></div><div><strong>Chinese</strong><span>Native</span></div></div></div></div></section>
<section id="contact" class="contact-band"><div><h2>Let’s talk robotics.</h2><p>For project discussions, research collaborations or engineering opportunities, I’d be happy to hear from you.</p></div><div class="contact-links">{link('mailto:jiayi.zhao@tum.de','jiayi.zhao@tum.de','contact-email')}<div class="socials">{link(GITHUB.rstrip('/'),'GitHub')}{link('https://www.linkedin.com/in/jiayi-zhao-251452430/','LinkedIn')}</div></div></section></div>'''
    return shell('Robotics, from algorithms to hardware', 'Jiayi Zhao: robotics engineer and TUM master’s student. Explore projects in motion planning, machine learning, embedded systems and mechatronics.', content)

if __name__ == '__main__':
    (ROOT/'index.html').write_text(homepage(),encoding='utf-8')
    for i, project in enumerate(PROJECTS):
        (ROOT/(project['slug']+'.html')).write_text(case_study(project, PROJECTS[(i+1)%len(PROJECTS)]),encoding='utf-8')
    print('Built homepage and four case studies.')
