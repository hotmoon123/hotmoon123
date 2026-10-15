# StitchLedger visual asset system — v0.2.2

## Decision and scope

**Design phase:** craft/production update, based on an already-established product brief. The design question is not “how many pictures can the app contain?” It is “which visual assets improve recognition, comprehension or platform integration without adding clutter?”

StitchLedger is a working mobile system for tailoring orders, deadlines and payment records. Its visual language must communicate **calm craft, accountable records and practical focus**—not fashion-magazine decoration, generic startup gradients, or AI-generated people at sewing machines.

### Existing product brief applied

| Brief element | Decision |
|---|---|
| Vision | Give small tailoring studios a dependable operating system for work and money records. |
| Primary user | A tailor, dressmaker, fashion designer or small-studio owner working quickly on a phone. |
| Single visual message | **Craft, in order.** |
| Context | App icon at 16–1024 px; Android/iPhone launch; small notification tray; compact mobile screens. |
| Tone | Practical, composed, warm, capable—not luxury theatre and not a generic finance app. |
| Anti-goals | No stock photography, AI portrait imagery, gradients used as hierarchy, decorative fabric textures, financial clichés, or competing hero illustrations. |

## Concept: `Cut + Keep`

The mark uses a single tailoring-scissors silhouette. The scissors communicate the physical craft; the product name and ordered UI communicate the record-keeping system. The mark is deliberately simple because an application icon must survive at small sizes, in monochrome, behind platform masks, and as an Android notification silhouette.

It does **not** attempt to draw a garment, cash, a spreadsheet and scissors in one square. That would fail the small-size and dominance tests.

## Asset inventory

A visual overview is available at `docs/visual-asset-preview.png`.

All assets are original geometric artwork produced for this project. They are not stock images, copied logos, or generated celebrity/customer imagery.

| Asset | Location | Use | Production property |
|---|---|---|---|
| Canonical source mark | `mobile/assets/app-icon.svg` | Master scalable source for the app tile | SVG, 1024×1024 viewBox |
| iOS/general app tile | `mobile/assets/icon.png` | Expo/iOS app icon and default Android icon | 1024×1024 RGBA, green full-bleed background |
| Transparent cream mark | `mobile/assets/brand-mark.svg` and `.png` | In-app wordmark tile on green background; monochrome source | SVG and 512×512 transparent PNG |
| Android adaptive foreground | `mobile/assets/adaptive-foreground.svg` and `adaptive-icon-foreground.png` | Android adaptive-icon safe foreground | SVG and 432×432 transparent PNG |
| Launch mark | `mobile/assets/splash-mark.svg` and `splash-icon.png` | Native launch screen over the cream background | SVG and 600×600 transparent PNG |
| Notification silhouette | `mobile/assets/notification-icon.svg` and `.png` | Small Android notification icon | 96×96 white-on-transparent PNG, no text/colour |

The app configuration assigns the tile, Android adaptive icon, launch asset, notification icon and notification colour. The app UI now uses the same transparent brand mark in its sign-in and desktop sidebar lockups.

## Deliberate exclusions

No additional in-app illustrations were added. This is intentional, not incomplete.

| Potential image | Decision | Reason |
|---|---|---|
| Stock photos of tailors/customers | Excluded | Adds rights, privacy, cultural-representation and download/performance risk without helping the daily task. |
| AI fashion-model art | Excluded | Does not improve order entry or financial accuracy; likely to date quickly and undermine trust. |
| Decorative empty-state art | Excluded | The existing simple icon/text/action pattern is clearer and lighter. |
| Workflow-status images | Excluded | Status requires unambiguous text, colour-independent labels and buttons, not illustrations users must interpret. |
| Money/deposit imagery | Excluded | Amounts, labels and ledger history are more precise than cash imagery. |
| Store screenshots/feature graphics | Deferred | Store dimensions, final signed build, privacy disclosures, trademark clearance and final marketing claim require a release brief. |

This keeps one dominant visual idea per surface and leaves operational screens focused on orders, due dates and amounts.

## Brand tokens and usage rules

| Role | Value | Rule |
|---|---|---|
| Studio green | `#275C46` | Primary brand field; use sparingly for decisive controls and icon background. |
| Paper | `#F6F5F0` | Primary warm application/splash background. |
| Ink | `#21382F` | Main text and high-emphasis content. |
| Muted | `#65736C` | Supporting text only; do not rely on it for small low-contrast text. |
| Alert red | `#A43E32` | Overdue/error signal with a text label; never colour alone. |
| Accent gold | `#A36B27` | Limited readiness/progress accent, not a second brand colour. |

### Do

- Use the full tile only as an app/store/profile icon.
- Use `brand-mark` only on a green field with sufficient clear space.
- Use the notification silhouette only as white artwork on transparent background; Android applies the notification colour.
- Keep the product name as selectable native text, not as a raster image, so it scales, localises and works with accessibility tools.
- Test the mark at 16 px, 48 px, 180 px and 1024 px before a public release.

### Do not

- Stretch, skew, outline, shadow or recolour the mark arbitrarily.
- Place the cream mark on a light/low-contrast field.
- Add a background to the Android notification PNG.
- Put a customer name, garment description, payment amount or balance inside notification graphics.
- Treat this work as trademark registration, clearance, legal advice or proof that the mark is available in a particular class or jurisdiction.

## Anti-slop review

The supplied Great Loop protocol was applied as a production/critique checklist:

- **One message per surface:** one scissors mark; no competing sewing, money and spreadsheet metaphors.
- **Dominance:** single mark on a plain field; no secondary decorative elements.
- **Greyscale and small-size logic:** mark carries meaning by silhouette and contrast rather than colour alone.
- **No trend stacking:** no mesh, glow, glass, abstract blobs, gradient or texture.
- **Production awareness:** vector master sources, platform-specific raster derivatives, Android adaptive safe area and all-white notification treatment are provided.
- **No invented clearance claim:** the work is original, but trademark, app-store and jurisdictional clearance remain an owner/legal review task.

## Accessibility and platform constraints

The visual identity supports but does not substitute for interface accessibility. The app continues to use visible text labels for workflows and status; icons are supplemental. The relevant user-interface contrast and non-colour principles are covered by WCAG 2.2, particularly the requirements concerning contrast and use of colour: https://www.w3.org/TR/WCAG22/.

Android notification icons are intentionally constrained by the operating system to monochrome artwork. Expo’s notification configuration supports an Android local icon and colour, while actual remote-push capability has separate development-build and credential requirements. See: https://docs.expo.dev/versions/latest/sdk/notifications/.

## Verification record

- PNG dimensions, alpha channels and transparent/opaque fields were inspected.
- `npm run typecheck` passed after the in-app brand-mark use was added.
- Expo web, Android and iOS JavaScript exports passed with the assets bundled.
- `npx expo prebuild --platform all --no-install` passed, regenerating native projects from the asset configuration.
- No signed APK/IPA, App Store/Play Store review, trademark search or physical-device icon/splash test is claimed complete.

## Next release gate

Before public release, install a signed test build on representative Android/iPhone devices and inspect:

1. icon masking/cropping on Android launchers;
2. iOS icon rendering and launch image;
3. notification icon legibility in light/dark system UI;
4. large-text/contrast behaviour of the UI labels beside icons;
5. actual store asset requirements and current platform policy;
6. trademark and commercial-use clearance appropriate to the owner’s market.
