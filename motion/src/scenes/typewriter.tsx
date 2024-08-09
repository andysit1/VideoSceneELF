



// https://github.com/danferns/motion-canvas-typewriter/blob/main/src/scenes/Typewriter.tsx  CREDIT: https://github.com/danferns

import { Txt, TxtProps, initial, signal } from "@motion-canvas/2d";
import { SignalValue, SimpleSignal, createSignal, useRandom, waitFor } from "@motion-canvas/core";

export interface TypewriterProps extends TxtProps {
    message: SignalValue<string>;
    fixWidth: SignalValue<boolean>;
}

export class Typewriter extends Txt {
    @signal()
    public declare readonly message: SimpleSignal<string, this>;

    @initial(false)
    @signal()
    public declare readonly fixWidth: SimpleSignal<boolean, this>;

    private readonly writtenText = createSignal("");
    constructor(props?: TypewriterProps) {
        super({
            ...props,
        });

        this.text(this.writtenText);

        if (props.fixWidth) {
            // prevent moving text as it's being typed
            this.setTextboxWidth();
        }
    }

    public *typewrite(seconds: number = undefined) {
        const timeDelays = [];
        let speedScaling = 1;
        for (let i = 0; i < this.message().length; i++) {
            timeDelays.push(generateTimeDelay(this.message(), i));
        }

        if (seconds !== undefined) {
            // normalize time delays to fit the given duration
            const totalTime = timeDelays.reduce((a, b) => a + b, 0);
            speedScaling = seconds / totalTime;
        }

        for (let i = 0; i < this.message().length; i++) {
            this.writtenText(this.message().slice(0, i + 1));
            yield* waitFor(timeDelays[i] * speedScaling);
        }
    }

    private setTextboxWidth() {
        this.writtenText(this.message());
        this.width(this.width());
        this.writtenText("");
    }
}

function generateTimeDelay(message: string, nextChar: number) {
    const char = message[nextChar + 1] || "";
    const random = useRandom();
    if (char === " ") {
        return random.gauss(0.15, 0.025);
    } else if (".,'".includes(char) && char !== "") {
        return random.gauss(0.2, 0.025);
    } else {
        return random.gauss(0.13, 0.025);
    }
}