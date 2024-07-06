module fsm (
    input clk,
    input rst_b,
    input i_en,
    output [2:0] o_state
);

typedef enum logic [2:0] { IDLE, ST1, ST2, ST3, OTHER } state;
state fsm_cs, fsm_ns;
always_ff @( posedge clk or negedge rsn_n ) begin : update_state
    if (!rst_n) begin
        fsm_cs <= IDLE;
    end else begin
        if (i_en) begin
            fsm_cs <= fsm_ns;
        end
    end
end

always_comb begin : func_state
    case (fsm_cs)
        IDLE: fsm_ns = ST1;
        ST1: fsm_ns = ST2;
        ST2: fsm_ns = ST3;
        ST3: fsm_ns = OTHER;
        default: fsm_ns = OTHER;
    endcase    
end
endmodule