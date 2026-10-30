import { useRef, type MutableRefObject } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

type PointerPosition = { x: number; y: number };
type ThreeAccentProps = {
  reducedMotion: boolean;
  pointer: MutableRefObject<PointerPosition>;
};

function SamosaAccent({ reducedMotion, pointer }: ThreeAccentProps) {
  const group = useRef<THREE.Group>(null);

  useFrame((_, delta) => {
    if (!group.current || reducedMotion) return;
    const targetX = pointer.current.y * 0.12;
    const targetY = pointer.current.x * 0.12;
    group.current.rotation.x = THREE.MathUtils.damp(group.current.rotation.x, targetX, 3, delta);
    group.current.rotation.y = THREE.MathUtils.damp(group.current.rotation.y + delta * 0.1, targetY, 2, delta);
  });

  return (
    <group ref={group} rotation={[0.18, -0.24, -0.12]}>
      <mesh scale={[1.08, 0.92, 0.56]}>
        <tetrahedronGeometry args={[0.78, 0]} />
        <meshStandardMaterial color="#D5A12E" roughness={0.82} metalness={0.02} flatShading />
      </mesh>
    </group>
  );
}

export default function ThreeAccent({ reducedMotion, pointer }: ThreeAccentProps) {
  return (
    <Canvas
      camera={{ position: [0, 0, 4], fov: 38 }}
      dpr={[1, 1.25]}
      frameloop={reducedMotion ? 'demand' : 'always'}
      gl={{ alpha: true, antialias: true, powerPreference: 'low-power' }}
      aria-hidden="true"
    >
      <ambientLight intensity={1.8} />
      <directionalLight position={[2, 3, 4]} intensity={2.1} color="#FFF7E8" />
      <SamosaAccent reducedMotion={reducedMotion} pointer={pointer} />
    </Canvas>
  );
}
